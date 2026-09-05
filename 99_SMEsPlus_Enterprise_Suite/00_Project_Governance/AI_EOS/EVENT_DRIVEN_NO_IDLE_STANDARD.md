# EVENT-DRIVEN / NO-IDLE EXECUTION STANDARD

Status: BOSS APPROVED — PILOT STANDARD  
Effective Date: 2026-09-05

## Principle

AI agents execute only when executable work exists.

> Waiting is not execution.

## Mandatory Stop Rule

When all currently executable work is complete:

1. Persist evidence.
2. Update `CHECKPOINT_REGISTER`.
3. Update `AUTO_RESUME_STATE`.
4. Commit/push where permitted.
5. Record unresolved dependencies.
6. Record exact `NEXT_ACTION`.
7. STOP the Claude Desktop/Web execution.

Do not poll continuously.
Do not remain active merely to wait for Boss, ChatGPT, peers, approvals, new commits, or external evidence.

## Resume Events

During the no-API pilot, a human starts/resumes Claude Desktop/Web when one of these material events occurs:

- `NEW_CONTROL_PROMPT_COMMITTED`
- `NEW_PEER_EVIDENCE_COMMITTED`
- `DEPENDENCY_RESOLVED`
- `NEW_DATABASE_EVIDENCE_AVAILABLE`
- `NEW_RUNTIME_EVIDENCE_AVAILABLE`
- `CONSTITUTION_CORRECTION_COMMITTED`
- `BOSS_CONTROLLED_DECISION_COMMITTED`
- `TOOL_OR_PERMISSION_BLOCKER_RESOLVED`

## Token Economy Rule

Token economy must come from:

- delta processing
- persistent state
- checkpoint resume
- peer last-consumed SHA tracking
- event-driven activation
- no idle waiting
- no repeated work without Material Delta

Token economy must NOT come from:

- skipping evidence
- shrinking a denominator
- skipping AAS-03 challenge
- skipping AAS+
- skipping PMO
- skipping gates
- premature closure

## Event Boundary

```text
EXECUTE
  ↓
CAPTURE EVIDENCE
  ↓
COMMIT RESULT + CHECKPOINT + AUTO_RESUME_STATE
  ↓
STOP CLAUDE

----- EVENT BOUNDARY -----

ChatGPT/Core Team reviews GitHub delta
  ↓
NEW CONTROL PROMPT / CORRECTION committed
  ↓
Human resumes OLD Claude Session
  ↓
Claude reads state + delta
  ↓
RESUME EXACT CHECKPOINT
```

## Pilot Limitation

There is no automatic GitHub → Claude Desktop/Web launch in this pilot.

Do not implement unsupported UI automation to simulate an API.

The manual dispatch step is accepted while cost and operating behavior are measured.
