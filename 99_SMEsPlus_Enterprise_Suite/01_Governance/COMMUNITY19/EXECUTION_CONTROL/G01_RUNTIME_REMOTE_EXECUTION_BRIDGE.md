# G01 Runtime Remote Execution Bridge

Status: ACTIVE
Authority: Boss
Controller: Claude Code
Remote worker: authorized Mac device `THPATTARAKRIT-SOLUTION-SERVICE-2.local`

LANE A is not part of this execution path.

## Control flow

Runtime Case Register
-> Claude Code classifies/selects work
-> scoped job in `EXECUTION_CONTROL/G01_RUNTIME_REMOTE_QUEUE.tsv`
-> remote worker executes when available
-> evidence returned
-> Claude Code reconciles
-> next job / A3 / remediation / MASTER

## Rules

- Mac offline = transport blocker only.
- Do not wait for Boss to select technical method.
- Do not stop controller-side work because remote worker is offline.
- Jobs must be explicit and bounded.
- Remote results must include case ID, environment, user/session class, observed result, evidence pointer, and disposition.
- Retest-required INCONCLUSIVE cases remain open work until closed or validly blocked.

No Evidence = No Progress.
