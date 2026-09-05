# AI_EOS_DISPATCHER_PHASE_0_5_PILOT.md

Version: Pilot v0.1
Status: BOSS APPROVED — PHASE 0.5 PREPARATION
Effective Date: 2026-09-05
Project: SMEsPlus ENTERPRISE SUITE
Mode: NO API — Claude Desktop/Web only

## 1. Objective

Pilot one persistent Claude controller/dispatcher session that reads compact GitHub control state and routes work to the appropriate execution session/task without performing the deep research itself.

The goal is to reduce Boss manual dispatch work and reduce token/usage waste from multiple worker sessions independently checking whether new work exists.

## 2. Core Pattern

ChatGPT/Core Team
→ GitHub Control/Evidence Backbone
→ Claude AI-EOS Dispatcher
→ P01..P11 Worker Session/Task
→ GitHub Evidence/Result
→ STOP

The Dispatcher is a control-plane role, not a research worker.

## 3. Pilot Constraint

- No Anthropic API.
- No OpenAI API.
- Use Claude Desktop or Claude Web only.
- Prefer Claude Dispatch Beta where available.
- Do not automate browser UI through unsupported scripts during this pilot.
- Boss remains Sole Final Approver.

## 4. Dispatcher Responsibility

The Dispatcher may:

- read compact GitHub control packets;
- identify Project / Process / Target Worker;
- identify Old Session / logical session continuity state;
- identify Prompt ID / Branch / Base SHA;
- identify Last Verified Checkpoint;
- identify whether a peer/material delta exists;
- select the worker routing target;
- launch/dispatch a worker when native Dispatch permits;
- prepare a launcher when native routing to the old physical session is unavailable;
- record dispatch state;
- stop when no executable routing work remains.

The Dispatcher must NOT:

- perform deep research;
- adjudicate accounting architecture;
- make Boss decisions;
- close AAS+ vetoes;
- reinterpret evidence;
- replace P11 reconciliation;
- merge to SMEsPlus;
- wait idle for worker completion.

## 5. Model / Effort

Default Dispatcher recommendation:

- Claude Sonnet 5
- Effort MEDIUM

Pilot may test LOW for purely deterministic routing if the product UI supports it safely.

Escalation to higher effort is not allowed merely because the target worker is important.
The Dispatcher should route complex work to the correct worker rather than reason through it itself.

## 6. Logical Session Rule

One Business Process should maintain one Traceable Research Story.

Physical Claude Session may change if Dispatch creates a child task.
Logical Session identity must remain in GitHub.

Required logical session state:

- Project
- Process
- Session ID
- Parent Session
- Branch
- Prompt ID
- Base SHA
- Last Verified Checkpoint
- Current Checkpoint
- Next Exact Action
- Peer Last-Consumed SHA
- Open Blockers
- Open Contradictions
- AAS+ State
- PMO State
- Boss Gate State

NEW PHYSICAL SESSION != RESET.

## 7. Dispatcher Event Model

Supported control events for the pilot:

- NEW_CONTROL_PROMPT_COMMITTED
- NEW_PEER_MATERIAL_DELTA
- READY_TO_RESUME
- DEPENDENCY_RESOLVED
- CORRECTION_REQUIRED
- READY_FOR_CORE_RECONCILIATION
- READY_FOR_BOSS_FINAL_GATE

The Dispatcher must ignore duplicate/non-material events.

## 8. No-Idle Rule

The Dispatcher must not remain active waiting for:

- Boss;
- workers;
- GitHub changes;
- peer completion;
- approvals;
- external evidence.

When routing work is complete:

READ → ROUTE → RECORD → STOP.

Waiting is not execution.

## 9. Worker Execution Rule

Worker session/task receives a compact launcher and reads the full control prompt/state from GitHub.

Worker behavior:

READ GitHub Control Packet
→ Read AUTO_RESUME_STATE
→ Read CHECKPOINT_REGISTER
→ Read only material delta
→ Execute
→ Evidence
→ Checkpoint
→ Commit / Push
→ Update AUTO_RESUME_STATE
→ STOP

Worker must not poll while waiting.

## 10. Pilot Test Scope

Start with ONE non-destructive existing accounting process before attempting broad P01-P11 orchestration.

Recommended candidates:

- P06 Bank-to-Reconcile, or
- P09 Plan-to-Analyze

Do not use P11 as the first technical routing experiment because P11 is the central reconciliation path and carries Boss-decision packaging risk.

## 11. Pilot Questions

The pilot must answer with evidence:

1. Can Claude Dispatch route work to an existing Old Session directly?
2. If not, can a child task safely continue the same Logical Session from GitHub state?
3. Can Dispatcher operate at Sonnet 5 MEDIUM without routing errors?
4. How much manual Boss interaction remains?
5. Does Dispatcher reduce worker idle/checking usage?
6. Can Last Verified Checkpoint be preserved across physical task changes?
7. Can duplicate dispatch be prevented procedurally?
8. Can P11 later consume worker commits delta-only without session-memory dependence?

## 12. Measurements

Record for each pilot dispatch:

- Control Event ID
- Dispatcher Model
- Dispatcher Effort
- Target Process
- Physical Target Type: OLD_SESSION / CHILD_TASK / MANUAL_LAUNCHER
- Start Time
- End Time
- Boss Manual Steps
- Worker Model/Effort
- Base SHA
- Result SHA
- Last Checkpoint Before
- Last Checkpoint After
- Duplicate Trigger? yes/no
- Routing Error? yes/no
- Continuity Error? yes/no
- Usage/limit observation visible in UI, if available

Do not invent token counts that the UI does not expose.

## 13. Acceptance Criteria

Phase 0.5 pilot is acceptable if:

- one dispatcher can route at least one real process safely;
- worker execution preserves GitHub lineage;
- no reset is required;
- Boss manual steps are reduced;
- no unsupported API is used;
- no worker is left idle waiting;
- no Boss-only decision is made by Dispatcher;
- result is committed and traceable.

## 14. Failure / Fallback

If native Dispatch cannot target an existing Old Session:

Fallback A:
Dispatcher prepares the exact Old-Session launcher; Boss sends it manually.

Fallback B:
Dispatcher spawns a child worker whose Logical Session is restored from GitHub state.

Do not abandon Old Session continuity semantics merely because the physical task container changes.

## 15. Governance

No Evidence = No Progress.
Never Skip Gate.
Old Session First.
New Prompt != New Session.
Scope-aware Everywhere.
Boss = Sole Final Approver.

## 16. Current Status

AI-EOS Phase 0.5 — PREPARED FOR CLAUDE DISPATCH PILOT.

No API enabled.
No automatic merge enabled.
No production execution authorized.
