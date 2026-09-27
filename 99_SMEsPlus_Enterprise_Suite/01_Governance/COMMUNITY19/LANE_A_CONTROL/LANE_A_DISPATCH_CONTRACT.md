# LANE A -> Claude Code Dispatch Contract

Status: ACTIVE
Authority: Boss
Operating mode: DELTA-FIRST / NO EVIDENCE = NO PROGRESS

## Purpose
Make LANE A work dispatch explicit, auditable, and machine-readable. Claude Code is an Executor, not the authority that invents scope or bypasses gates.

## State machine
READY_FOR_EXECUTION -> IN_PROGRESS -> EVIDENCE_SUBMITTED -> ACCEPTED
                                           |-> REMEDIATION_REQUIRED -> IN_PROGRESS
                                           |-> HOLD

## Mandatory task fields
- task_id
- source_lane
- owner
- group_scope
- objective
- input_artifacts
- required_outputs
- acceptance_criteria
- evidence_required
- prohibited_actions
- return_path
- status

## Dispatch rule
1. LANE A creates/updates a task artifact and Task Register row.
2. Claude Code may execute only tasks in READY_FOR_EXECUTION or a Boss-authorized task already IN_PROGRESS.
3. Claude Code must write results/evidence to the declared return path and set EVIDENCE_SUBMITTED.
4. LANE A / Independent Review checks evidence.
5. Only LANE A / governed reviewer changes disposition to ACCEPTED, REMEDIATION_REQUIRED, or HOLD.
6. Boss remains sole Final Approver for Freeze / Final Approval where required.

## Prohibited
- Claude Code must not create a parallel governance framework.
- No inferred module membership may be promoted without evidence.
- No Formal Coverage before Boss-frozen denominator.
- No silent overwrite/delete of prior evidence.
- No merge/freeze/final approval unless explicitly authorized.


## Standing Auto-Pickup Authorization — Boss 2026-09-28

When Claude Code completes its current governed task and there is no new explicit LANE A command waiting:

1. Read `LANE_A_CONTROL/LANE_A_AUTO_PICKUP_QUEUE.tsv`.
2. Select the highest-readiness G that is not already IN_PROGRESS, EVIDENCE_SUBMITTED, HOLD, or ACCEPTED.
3. Record the selected G in `LANE_A_TASK_REGISTER.tsv` with `source=CLAUDE_CODE_AUTO_PICKUP` in the objective/notes of the task artifact.
4. Execute only LANE A intake/reconciliation work for that G.
5. Continue until `EVIDENCE_SUBMITTED`.
6. Do not self-declare `LANE_A_PASS`, A1 admission, Boss approval, canonical freeze, or Formal Coverage.
7. If the selected G becomes blocked, record the blocker and move to the next independently executable G.
8. Never invent module membership to make a group count match.

Selection criteria, in order:
- exact or near-exact module-name evidence available;
- existing governed/source evidence pointers available;
- existing GMVQ Question Banks available;
- no unresolved cross-group ownership conflict that prevents useful intake;
- highest amount of executable evidence-backed work remaining.

This standing authorization removes the need to wait idle for Boss or LANE A to manually issue every next G task. It does not weaken any gate.


## Mandatory Cross-Branch Evidence Bridge

Before any LANE A task concludes `NOT_FOUND`, `NO BANK`, `0 MODULE`, or absence-based HOLD, it MUST read:

- `LANE_A_CONTROL/GMVQ_LANE_A_EVIDENCE_BRIDGE.md`

This bridge requires checking both:
- `SmEsPlus` canonical/control tree, and
- PR #71 candidate evidence branch/path.

Branch-local absence is not project-wide absence.
