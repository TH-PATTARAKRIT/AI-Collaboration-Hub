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
