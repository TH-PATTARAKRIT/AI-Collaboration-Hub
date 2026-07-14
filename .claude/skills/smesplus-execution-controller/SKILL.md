---
name: smesplus-execution-controller
description: control all claude code execution for the smesplus enterprise suite across governance, architecture, functional design, development, qa, database, infrastructure, migration, evidence, github, and closure work. use this skill whenever claude code receives a smesplus task, must select a model, execute non-interactively, manage risk and authority, create evidence, coordinate review and verification, resume work across sessions, or prepare a boss decision pack.
---

# SMEsPlus Execution Controller

Apply this skill before executing any SMEsPlus Claude Code task.

## Operating sequence

1. Read the current order, repository context, related issue or PR, and any session handoff.
2. Build an execution contract containing session, state, step, objective, scope, mode, deliverables, acceptance criteria, evidence, and stop conditions.
3. Classify work type, risk, write mode, and required model using `references/master-control.md`.
4. Load the relevant State rules from `references/state-workflows.md`.
5. Execute all pre-authorized, reversible work without asking for routine confirmation.
6. Apply repository, evidence, review, verification, clean-room, security, and traceability controls from `references/governance-controls.md`.
7. Use `references/decision-and-handoff.md` for true Stop Conditions, Boss decisions, recovery, and multi-session handoff.
8. Use `templates/execution-order.md` to normalize incomplete orders and `templates/final-report.md` for the final report.

## Mandatory behavior

- Continue automatically within approved scope.
- Do not ask open-ended questions.
- Do not ask Boss to reconfirm an instruction already present in the order or an existing approval record.
- Select the safest reversible option for LOW or MEDIUM risk work and record the assumption.
- Stop only the restricted action when a defined Stop Condition applies; continue all other permitted work.
- Consolidate all true Boss decisions into one Decision Pack with options, reasons, impact, risk, recommendation, and safe default.
- Never treat silence as approval for Final Gate, Merge, Release, Deployment, Production, State Closure, authority changes, destructive operations, or secrets.
- Never self-review, self-verify, self-approve, or declare PASS/CLOSED without the required independent evidence and Boss decision.
- Preserve Git history, rollback capability, evidence paths, timestamps, commit SHAs, and role separation.
- Treat HOLD as gate restriction, not as a stop to permitted preparation and evidence work.

## Completion states

Classify every task as exactly one of:

- COMPLETED WITH EVIDENCE
- READY FOR INDEPENDENT REVIEW
- READY FOR INDEPENDENT VERIFICATION
- BOSS DECISION REQUIRED
- BLOCKED BY STOP CONDITION

Never leave an executable task as WAITING FOR CONFIRMATION when no Stop Condition exists.
