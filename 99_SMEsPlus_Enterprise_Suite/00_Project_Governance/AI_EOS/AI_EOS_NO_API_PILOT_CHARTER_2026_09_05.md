# AI-EOS NO-API PILOT CHARTER — 2026-09-05

Status: BOSS APPROVED — CONTROLLED PILOT PREPARATION  
Project: SMEsPlus ENTERPRISE SUITE  
Boss: Sole Final Approver

## 1. Decision

The project will prepare the AI Engineering Operating System (AI-EOS) using SMEsPlus as the reference implementation.

Current pilot constraint:

> **Do not use OpenAI API or Anthropic API. Use Claude Desktop or Claude Web only for Claude execution while actual cost and operating behavior are evaluated.**

This constraint supersedes any earlier recommendation that implied immediate API-based orchestration.

## 2. Pilot Objective

Prove the operating model before automating it.

Measure:

- Claude Desktop/Web usage and cost behavior
- token/context efficiency
- interruption and resume quality
- evidence completeness
- research depth
- parallel-process throughput
- human orchestration effort
- GitHub traceability
- cross-process reconciliation quality
- Boss Final Gate quality

## 3. Current Approved Architecture

```text
                            BOSS
                     SOLE FINAL APPROVER
                              ▲
                              │
                       BOSS FINAL GATE
                              │
                    ChatGPT / Core Team
              Architecture / PMO / Audit / Control
                              ⇅
                            GitHub
         Canonical Prompt / Evidence / State / Audit Lineage
                              ⇅
                  Claude Desktop / Claude Web
                     Autonomous Executor
                              ⇅
            Source / DB / Runtime / Playwright / Tests
                              │
                              ▼
                            GitHub
```

## 4. Human-in-the-Loop Dispatch

During this pilot GitHub is the control queue, but it does not directly invoke Claude Desktop/Web.

Approved sequence:

```text
Claude executes
→ commits result/evidence/state to GitHub
→ Claude stops
→ ChatGPT/Core Team reads GitHub delta
→ ChatGPT produces review / correction / NEW PROMPT
→ NEW PROMPT is persisted to GitHub
→ Boss/operator opens or resumes the existing Claude Desktop/Web Session
→ Claude reads the GitHub control packet
→ Claude resumes from the recorded checkpoint
```

The manual launch step is intentional during the no-API cost-evaluation period.

## 5. Session Continuity

Default:

> **OLD SESSION FIRST**

Rules:

- NEW PROMPT does not require NEW SESSION.
- Material Delta should normally be processed in the existing Session.
- Checkpoint continuation stays inside the existing Session when technically possible.
- New Session is allowed only for material execution reasons or explicit Boss direction.
- New Session never means reset.

## 6. Persistent State

Each long-running process should maintain, where applicable:

- `CHECKPOINT_REGISTER`
- `AUTO_RESUME_STATE`
- `CURRENT_STATE`
- `EVIDENCE_MANIFEST`
- `SOURCE_LINK_REGISTER`
- `CONTRADICTION_REGISTER`
- `DEPENDENCY_REGISTER`
- `RESEARCH_ERROR_AND_REVISION_LOG`
- peer `LAST_CONSUMED_SHA`
- exact `NEXT_ACTION`

Conversation history is supporting context. GitHub state is the recoverable project record.

## 7. No-Idle-Token Rule

AI agents must not remain active merely to wait for:

- Boss input
- ChatGPT review
- peer completion
- approval
- new evidence
- new commits
- external dependencies

When no executable work remains:

1. persist evidence;
2. update checkpoint state;
3. update auto-resume state;
4. commit/push where permitted;
5. record open dependencies;
6. record exact next action;
7. stop execution.

Waiting is not execution.

## 8. Parallel Research Model

P01–P10 may execute in parallel.

P11 performs continuous reconciliation from published evidence and peer deltas.

Conceptual flow:

```text
P01 ─┐
P02 ─┤
P03 ─┤
...  ├──> GitHub Evidence ──> P11 Reconciliation ──> Boss Final Gate
P10 ─┘
```

No Process should wait for all peers if unaffected work can continue.

## 9. Decision Authority

- Peer Position != Peer Decision
- Peer Decision != Boss Decision
- UNRESOLVED != ADOPTED
- Recommendation != Canonical Boundary
- Design Candidate != Approved Architecture
- PMO Recommendation != Boss Final Approval

Boss remains the sole final approver.

## 10. Evidence Integrity

Mandatory review order:

1. Evidence Population
2. Denominator
3. Tool Capability
4. Extraction Completeness
5. Extracted Evidence vs Reviewed Evidence
6. Finding
7. Cross-Process Challenge
8. Decision Authority

No Evidence = No Progress.
Never Skip Gate.

## 11. Deferred Automation

The following are explicitly deferred until Boss authorizes a later phase:

- automatic GitHub-to-Claude invocation
- Anthropic API
- OpenAI API
- automatic model dispatch
- autonomous API-based reviewer agents
- Temporal workflow runtime
- production AI Agent Orchestrator

Preparation of standards, state files, event schemas, and pilot measurements is allowed.

## 12. Dropbox

Dropbox is a publication/archive layer, not the active engineering source of truth.

Approved documents may be copied to Dropbox after controlled project approval/closure.

## 13. Pilot Exit

The pilot does not end based on elapsed time.

Pilot evaluation must be evidence-based and include:

- cost observations
- agent utilization
- idle avoidance
- resume success
- research completeness
- defect discovery quality
- cross-process contradictions
- manual coordination overhead
- recommendation for Phase 1.

No API transition occurs automatically at pilot exit.
Boss decides the next phase.
