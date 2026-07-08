# SMEsPlus State-Based Claude Skill Lifecycle Control v0.1

Document ID: SMEPLUS-SKILL-LIFECYCLE-001
Version: v0.1
Control Level: /L99
Status: PREPARED IN GITHUB / CHATGPT L99 REVIEW REQUIRED / NOT APPROVED / NOT AUTOMATED YET
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Branch: SMEsPlus
Path: `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/Skill_Design/SMEsPlus_STATE_BASED_SKILL_LIFECYCLE_CONTROL_v0.1.md`
Generated: 2026-07-08 (Asia/Bangkok)

## Executive Summary

Boss clarified that SMEsPlus must not create all Claude Skills too early as fixed artifacts. A Skill that is well designed today may fail during real execution if upstream data, FDS, repository structure, evidence paths, workflows, or gate rules change.

Therefore, SMEsPlus will use a State-Based Skill Lifecycle.

Control decision:

```text
Do not build all Skills upfront.
Create or refresh each Skill immediately before the State where it will be used.
Validate the Skill against the latest GitHub, evidence, FDS, RACI, Make payload, and gate status before activation.
```

## 1. Core Principle

A Claude Skill is not a permanent truth source.

A Claude Skill is an execution helper that must be synchronized with the latest project source of truth before use.

Current source of truth priority:

```text
1. GitHub verified file / commit / path
2. PMO evidence register
3. Jira / execution ticket where applicable
4. Google Drive evidence archive where applicable
5. Boss explicit decision
6. ChatGPT L99 review result
```

If the source of truth changes, the Skill must be reviewed or regenerated before use.

## 2. State-Based Skill Lifecycle

For every project State, follow this sequence:

```text
State planning
-> Identify required Owner work
-> Identify required Skill or Skill refresh
-> Snapshot latest source evidence
-> Design or update Skill blueprint
-> AI PMO owner lock
-> ChatGPT L99 review
-> Boss decision where required
-> Dry-run Skill output
-> Activate for that State only
-> Archive output and evidence
-> Freeze or retire Skill version after State completion
```

## 3. Skill Timing Rule

| Timing | Rule | Reason |
|---|---|---|
| Too early | Do not build operational Skill packages too far ahead of use | Upstream may change |
| Before State entry | Build or refresh Skill blueprint | Uses current evidence |
| During State | Skill may produce owner-level work output | Under AI PMO control |
| Before Gate | Skill output must be reviewed | Skill cannot pass gate |
| After State | Skill version must be archived or retired | Prevent stale reuse |

## 4. State Entry Skill Gate

Before a State starts, AI PMO must answer:

```text
1. What State is starting?
2. What Owner work is required?
3. What Skill is needed?
4. Is an existing Skill still valid?
5. What upstream data changed?
6. What GitHub commit/path is current?
7. What evidence register is current?
8. What gate rules are current?
9. Who reviews the Skill output?
10. Who approves final State movement?
```

If any answer is missing, the Skill must be marked:

```text
SKILL_REFRESH_REQUIRED / STATE ENTRY HOLD
```

## 5. Mandatory Skill Freshness Check

Before any Skill is used, check:

| Check | Required Evidence |
|---|---|
| Latest GitHub path exists | commit SHA + path |
| Latest FDS / design document confirmed | file path + version |
| Latest evidence register confirmed | path + timestamp |
| Latest RACI confirmed | path + commit SHA |
| Latest Make payload schema confirmed | schema path / version |
| Latest gate status confirmed | AI PMO / ChatGPT L99 note |
| Latest Boss decision confirmed | decision log / statement |

If freshness cannot be confirmed, do not use the Skill.

## 6. Skill Version Naming Standard

Use State-aware Skill versioning:

```text
<skill-name>__state-<NN>__v<major.minor>
```

Example:

```text
smesplus-expert-fds-designer__state-04__v0.1
qa-uat-package-generator__state-07__v0.1
make-automation-controller__state-08__v0.1
```

Do not reuse an old Skill version across States without a freshness check.

## 7. Skill Lifecycle Status Vocabulary

Allowed statuses:

```text
SKILL_BLUEPRINT_DRAFTED
SKILL_REFRESH_REQUIRED
SKILL_DESIGN_HOLD
SKILL_DRY_RUN_READY
SKILL_DRY_RUN_REVIEW_REQUIRED
SKILL_ACTIVE_FOR_STATE_ONLY
SKILL_ARCHIVED_AFTER_STATE
SKILL_RETIRED
```

Forbidden statuses:

```text
SKILL_APPROVED_FOR_GATE
SKILL_CAN_PASS_GATE
SKILL_PRODUCTION_READY
SKILL_FINAL_APPROVED
SKILL_COMPLETE
```

## 8. Recommended State Skill Strategy

| State | Skill Strategy |
|---|---|
| State 01 Project Identity | Use Skill blueprint only; no heavy automation |
| State 02 Governance | Create/refresh governance and AI PMO Skills |
| State 03 Architecture | Create/refresh architecture/API/DB review Skills |
| State 04 Functional Design | Create/refresh FDS and gap review Skills |
| State 05 UX/UI Design | Create/refresh UI handoff and design review Skills |
| State 06 Development | Create/refresh coding review support only; no gate bypass |
| State 07 Testing & QA | Create/refresh QA/UAT generator and defect review Skills |
| State 08 AI Execution | Create/refresh Make and AI routing Skills |
| State 09 Infrastructure & Deployment | Create/refresh infra evidence and deployment readiness Skills |
| State 10 Production Operations | Create/refresh production operations checklist Skills only after production approval |
| State 11 Knowledge Base | Create/refresh KB capture and training Skills |
| State 12 Current Execution Context | Refresh all active Skill assumptions before continuing |

## 9. Control Impact on Claude Skill Architect Controller

`claude-skill-architect-controller` must not design generic Skills in isolation.

It must design each Skill using the latest State context:

```text
current_state
current_module
current_repository_commit
current_evidence_paths
current_gate_status
current_owner_lock
current_reviewer
current_forbidden_actions
current_make_payload_schema
```

Any Skill missing State context must be rejected as:

```text
SKILL_DESIGN_HOLD / MISSING_STATE_CONTEXT
```

## 10. Gate Rule

A Skill may prepare work for a State.

A Skill may not approve State movement.

State movement still requires:

```text
AI PMO owner/evidence confirmation
ChatGPT L99 independent review
Boss final decision where required
```

## 11. Next Required Actions

1. Update Claude Skill Architect Controller prompt to include State-Based Skill Lifecycle.
2. Do not build all operational Skills at once.
3. Build or refresh Skill only before the State where it is needed.
4. Require freshness check before every Skill activation.
5. Archive or retire Skill version after each State.
6. Keep Make Automation HOLD until the State-based lifecycle is reviewed.

## Final Control Status

```text
State-Based Skill Lifecycle: PREPARED
Skill Package Build: HOLD
Claude Skill Architect Controller: MUST INCLUDE THIS RULE
AI PMO Review: REQUIRED
ChatGPT L99 Review: REQUIRED
Boss Decision: REQUIRED BEFORE ACTIVATION
```

PREPARED IN GITHUB / SKILL MUST BE STATE-FRESH / NOT APPROVED / NOT AUTOMATED YET
