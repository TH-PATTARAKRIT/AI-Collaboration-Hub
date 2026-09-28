# Claude Code Autonomous Execution Contract

Status: ACTIVE
Authority: Boss
Mode: DELTA-FIRST / EVIDENCE-FIRST / AUTO-CONTINUE

## Decision

LANE A is retired as an active dispatch/execution prerequisite.

Historical LANE A artifacts remain read-only audit evidence and MUST NOT be deleted or rewritten.

Claude Code is the active execution controller.

## Active execution chain

Claude Code
-> reconcile current governed state
-> choose next technically valid action
-> execute with available tools
-> capture evidence
-> reconcile result
-> Independent Review / A3 where required
-> remediation / retest
-> MASTER consolidation
-> recommendation
-> Boss decision

No separate LANE A dispatch is required.

## Autonomous authority

Claude Code may, without per-step Boss approval:
- choose RPC/API/UI/session/disposable-runtime methods;
- provision safe test users, groups, ACLs, fixtures, and scratch databases;
- create scoped remote jobs;
- continue to the next executable case or G;
- retry with a different valid technical method;
- reconcile evidence;
- run remediation and retest;
- proceed to A3/Independent Review after prerequisites are met.

## Mandatory constraints

Claude Code MUST NOT:
- change governance rules or canonical denominator;
- self-approve Boss gates;
- fabricate evidence;
- treat candidate evidence as canonical membership;
- use source-only evidence as runtime proof;
- use superuser RPC as access-control proof;
- perform destructive action on protected Production without explicit Boss authorization;
- erase superseded/failed evidence.

## Work selection

When current work completes:
1. read current execution state;
2. select highest-value evidence-backed executable work;
3. continue automatically;
4. if one path is blocked, record the exact blocker and move to another independent path;
5. stop only when no valid work remains or a true Boss/architecture decision is required.

No idle waiting for a dispatch layer.

No Evidence = No Progress.
Boss remains sole Final Approver.
