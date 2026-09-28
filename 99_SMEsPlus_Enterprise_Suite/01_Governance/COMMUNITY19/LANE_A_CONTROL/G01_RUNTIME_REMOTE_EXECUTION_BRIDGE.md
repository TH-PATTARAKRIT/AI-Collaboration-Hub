# G01 Runtime Remote Execution Bridge

Status: ACTIVE
Authority: Boss
Scope: G01 PLATFORM_BASE runtime closure
Primary executor split:
- Controller: Claude Code / repository-side session
- Remote Worker: authorized Mac device `THPATTARAKRIT-SOLUTION-SERVICE-2.local`

## Problem being solved

The repository-side Claude Code container cannot directly reach the runtime network used by `iTest19C`.
The authorized Mac device can act as the execution surface when online.

This bridge removes manual per-case Boss relaying.

## Control rule

Claude Code MUST NOT wait for Boss merely because its own container cannot reach the runtime.

Instead:
1. reconcile the next executable Runtime cases;
2. emit scoped jobs into `G01_RUNTIME_REMOTE_QUEUE.tsv`;
3. mark them `READY_FOR_REMOTE`;
4. when the authorized Mac worker is online, execute jobs in priority order;
5. write evidence/result records back to governed paths;
6. controller consumes completed results and continues automatically to the next batch.

## Worker availability states

- `ONLINE_READY`
- `OFFLINE_WAITING`
- `EXECUTING`
- `RESULT_SUBMITTED`
- `BLOCKED_REMOTE`

Physical device offline is a transport blocker only. It must NOT be rewritten as a permission or governance blocker.

## Job scope requirements

Every job must be narrow and explicit:
- job_id
- case_ids
- module
- execution_class (A_RPC / B_UI_SESSION / C_DISPOSABLE)
- target_environment
- required_user
- required_preconditions
- exact command/action boundary
- expected evidence
- return_path
- source_anchor
- destructive_flag

Do not submit an open-ended "do everything" remote charter.

## Auto-continuation

When remote worker is unavailable:
- continue all repository-side work;
- prepare subsequent remote jobs;
- reconcile evidence;
- do not idle waiting for Boss.

When worker returns online:
- process READY_FOR_REMOTE jobs automatically in queue order;
- no per-job Boss approval is required unless the job is destructive against protected Production or changes governance/scope.

## Result integrity

Remote results must include:
- execution timestamp
- device identity
- environment
- case ID
- user/session identity class
- observed result
- log/screenshot/response pointer
- PASS/FAIL/INCONCLUSIVE/BLOCKED
- reason
- commit SHA or returned artifact pointer

No Evidence = No Progress.
