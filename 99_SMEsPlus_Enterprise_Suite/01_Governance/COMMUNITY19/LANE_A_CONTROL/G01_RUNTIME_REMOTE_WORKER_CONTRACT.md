# G01 Runtime Remote Worker Contract

Worker device:
`THPATTARAKRIT-SOLUTION-SERVICE-2.local`

## On startup / reconnect

1. Pull latest `SMEsPlus`.
2. Read:
   - `LANE_A_CONTROL/G01_RUNTIME_REMOTE_EXECUTION_BRIDGE.md`
   - `LANE_A_CONTROL/G01_RUNTIME_REMOTE_QUEUE.tsv`
3. Select the highest-priority `READY_FOR_REMOTE` job.
4. Execute only the declared scope.
5. Capture evidence.
6. Write result into the declared return path.
7. Change queue state to `RESULT_SUBMITTED`.
8. Continue next READY_FOR_REMOTE job automatically.

## Do not ask Boss for technical method selection

Choose the valid method from:
- RPC/API
- authenticated non-superuser UI/session
- local terminal/process tooling
- disposable test DB/runtime
- controlled fixture provisioning

Escalate only for:
- destructive Production action
- unavailable credential/infrastructure not already authorized
- governance/scope/denominator change
- unresolved Critical/Zero-Tolerance decision

## Failure semantics

If a method fails, record it and try the next valid method.
If the device loses connectivity, record `BLOCKED_REMOTE` and preserve partial evidence.
Do not convert transport failure into product FAIL.
