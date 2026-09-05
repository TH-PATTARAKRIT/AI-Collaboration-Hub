# SESSION / CHECKPOINT / AUTO-RESUME STANDARD

Status: BOSS APPROVED — PILOT STANDARD  
Effective Date: 2026-09-05

## 1. Default Session Policy

**OLD SESSION FIRST.**

A NEW PROMPT does not require a NEW SESSION.

Use the existing Session for:

- Material Delta
- correction
- targeted closure
- peer reconciliation
- evidence refresh
- checkpoint reopen
- final-gate preparation

New Session is an exception for material execution reasons or explicit Boss direction.

## 2. New Session Continuity

If a New Session is required, preserve:

- Parent Session
- Parent Prompt
- Branch
- Last Verified Commit
- Last Verified Checkpoint
- Current Checkpoint/Substep
- Open Blockers
- Open Contradictions
- Open Dependencies
- Boss Controlled Decisions
- AAS+ state
- PMO state
- Peer Last-Consumed SHAs
- Exact Next Action

NEW SESSION != RESET.

## 3. Checkpoint Status

Every checkpoint is exactly one of:

- `NOT_STARTED`
- `IN_PROGRESS`
- `COMPLETE_EVIDENCE_VERIFIED`
- `PARTIAL_RESUMABLE`
- `BLOCKED_EXTERNAL_DEPENDENCY`
- `BLOCKED_TOOL_PERMISSION`
- `BLOCKED_EVIDENCE_REQUIRED`
- `SUPERSEDED_MATERIAL_DELTA`

## 4. Auto-Continue

After an internal checkpoint reaches `COMPLETE_EVIDENCE_VERIFIED`, continue to the next executable checkpoint automatically.

Do not ask Boss for routine continuation approval.

Checkpoint != Boss Gate.

## 5. Auto-Resume

On resume:

1. Read `AUTO_RESUME_STATE`.
2. Read `CHECKPOINT_REGISTER`.
3. Verify branch and current commit.
4. Identify the last verified checkpoint.
5. Identify the first incomplete checkpoint/substep.
6. Read only material delta and evidence required for that checkpoint.
7. Resume.

Do not reread the entire repository by default.
Do not repeat completed work without Material Delta.

## 6. Partial Resume

If interrupted within a checkpoint, persist:

- completed substeps
- remaining substeps
- evidence already acquired
- commands/queries already executed
- artifacts already modified
- unverified artifacts
- exact next substep

Resume from that exact point.

## 7. Peer-Aware Resume

Every parallel process should track peer `LAST_CONSUMED_SHA` values where relevant.

If a peer SHA is unchanged, do not reprocess the package.

If a peer publishes a materially changed SHA, reopen only the affected reconciliation checkpoint.

## 8. Material Delta Reopen

A completed checkpoint may be reopened only for a material reason such as:

- new source
- new database
- new runtime evidence
- new deployed module population
- new peer evidence
- denominator correction
- version correction
- constitutional correction
- Boss Controlled Decision
- material contradiction
- new authoritative statutory evidence

Preserve the original checkpoint result in revision lineage.

## 9. Exact Interruption Record

Before any stop/interruption record:

```text
LAST_VERIFIED_CHECKPOINT:
CURRENT_CHECKPOINT:
CURRENT_SUBSTEP:
CURRENT_STATUS:
LAST_VERIFIED_COMMIT:
OPEN_DEPENDENCIES:
OPEN_CONTRADICTIONS:
NEXT_EXACT_ACTION:
RESUME_MODE: AUTO
```

## 10. Final Gate

Auto-Continue and Auto-Resume apply to internal execution.

They stop at the defined Boss Final Gate.

No merge, production implementation, canonical architecture freeze, or final approval may be inferred from an internal checkpoint.
