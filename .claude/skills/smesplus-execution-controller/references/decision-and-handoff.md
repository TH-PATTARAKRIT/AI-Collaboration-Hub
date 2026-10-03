# Decision, Handoff, Recovery, and Completion Notification

## Anti-loop rule

Before asking Boss, search the current order, Boss Decision Register, Canonical authority documents, related Issue/PR, and Session Handoff. If the answer exists, cite it and continue. Do not ask again.

## Decision request

Never ask an open-ended question. A true Boss Decision Pack must include: Decision ID, exact decision, reason authority is required, materially different options, reason for each, impact, risk, reversibility, recommendation, recommendation reason, safe default, work that continues, evidence paths, and Gate impact.

Automatically select the recommended option when risk is LOW or MEDIUM, reversibility is FULL, Gate impact is NONE or HOLD, and the action is already authorized.

No response means HOLD for Final Gate, Merge, Release, Deployment, Production, State Closure, authority changes, destructive actions, or secrets. Silence is never approval.

## Stop conditions

Stop only the restricted action for: destructive or irreversible work, authority boundary, security/credentials, direct mandatory-instruction conflict with no safe interpretation, or unrecoverable technical failure. Continue every other permitted task and record the exception.

## Session handoff

Create or update: SESSION_HANDOFF.md, CURRENT_EXECUTION_CONTEXT.md, OPEN_DECISIONS.md, OPEN_EXCEPTIONS.md, NEXT_ACTIONS.md, and EVIDENCE_INDEX.md. Record From role, To role, task, authority, inputs, outputs, evidence, completion condition, and prohibited actions.

## Recovery

On resume, inspect last successful commit, branch, open PR, incomplete tasks, failed commands, pending review/verification, Boss decisions, and uncommitted files. Create RECOVERY_CHECKPOINT.md and continue from the last evidenced state.

## Mandatory completion notification

At the end of every prompt or execution order, send Boss a clear completion message. Do not end silently.

Use exactly one session disposition:

- READY TO ARCHIVE — all prompt-scoped executable work is completed with evidence and no follow-up execution remains in this session.
- KEEP SESSION ACTIVE — prompt-scoped execution is complete, but Independent Review, Verification, Boss Decision, or another linked action must still occur in the same session.
- BLOCKED — a defined Stop Condition prevents completion.

The notification must state:

1. `ดำเนินการตาม Prompt เสร็จแล้ว` or `Prompt execution completed`.
2. Session ID and title.
3. Completion state.
4. Branch, Commit SHA, Draft PR, Issue/Jira references.
5. Deliverables and validation summary.
6. Evidence level and Gate result.
7. Open decisions or exceptions.
8. Session disposition: READY TO ARCHIVE, KEEP SESSION ACTIVE, or BLOCKED.
9. Recommended archive folder/path when READY TO ARCHIVE.

Do not say READY TO ARCHIVE when review, verification, Boss decision, merge, or closure is still intended to be performed in the same session. Instead state KEEP SESSION ACTIVE and identify the exact remaining action.