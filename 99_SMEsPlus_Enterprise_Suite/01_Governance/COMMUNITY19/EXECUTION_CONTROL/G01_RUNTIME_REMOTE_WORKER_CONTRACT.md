# G01 Runtime Remote Worker Contract

Status: ACTIVE
Worker: `THPATTARAKRIT-SOLUTION-SERVICE-2.local`
Controller: Claude Code

LANE A is retired from active execution.

## Reference facts (for context, not a substitute for a session's own judgment)

- Target environment `iTest19C` (`103.253.74.217`) is a Boss-confirmed test/staging instance, not
  Production.
- This file, `EXECUTION_CONTROL/G01_RUNTIME_REMOTE_EXECUTION_BRIDGE.md`, and
  `EXECUTION_CONTROL/G01_RUNTIME_REMOTE_QUEUE.tsv` are the current control artifacts for this
  worker role.
- Boss's standing execution authorization for this workstream is recorded in
  `CLAUDE_CODE_AUTONOMOUS_EXECUTION_CONTRACT.md`.

Each session should still apply its own judgment and safety practices to what it actually executes
— this file provides context, not a directive to skip a session's own safety checks.

## On reconnect

1. Pull the active Claude Code branch and latest governed control artifacts.
2. Read `EXECUTION_CONTROL/G01_RUNTIME_REMOTE_QUEUE.tsv`.
3. Execute the highest-priority `READY_FOR_REMOTE` job.
4. Use the technically valid method without asking Boss:
   - RPC/API
   - authenticated non-superuser UI/session
   - terminal/process tooling
   - disposable scratch DB/runtime
   - controlled fixture provisioning
5. Capture evidence.
6. Write result to the declared return path.
7. Mark result state for controller reconciliation.
8. Continue automatically.

## Escalate only for

- destructive Production action;
- unavailable credential/infrastructure outside current authorization;
- governance/scope/denominator change;
- unresolved Critical/Zero-Tolerance business decision.

Transport failure is not product FAIL.
Superuser RPC is not valid access-control proof.
