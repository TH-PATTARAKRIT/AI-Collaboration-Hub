# SMEsPlus AI Engineering Operating System (AI-EOS)

Status: BOSS APPROVED — PILOT PREPARATION  
Effective Date: 2026-09-05  
Project: SMEsPlus ENTERPRISE SUITE  
Pilot Constraint: **NO OpenAI API / NO Anthropic API**  
Executor Interface: Claude Desktop or Claude Web only  
Control Interface: ChatGPT + GitHub  
Boss: Sole Final Approver

## Purpose

Use SMEsPlus as the reference implementation for a future company-wide AI Agent operating model.

The pilot control loop is:

```text
ChatGPT / Core Team
        ⇅
      GitHub
        ⇅
Claude Desktop / Web
```

GitHub is the canonical control and evidence backbone. Chat sessions are execution interfaces, not the project source of truth.

## Pilot Operating Model

```text
Boss Final Gate
      ▲
      │
ChatGPT / Core Team / PMO / Audit
      ⇅
GitHub — Prompt / Evidence / Checkpoint / Revision / Decision Lineage
      ⇅
Claude Desktop / Web — Executor
      ⇅
Source / DB / Runtime / Playwright / Test Evidence
```

## Mandatory Pilot Constraints

1. No OpenAI API integration.
2. No Anthropic API integration.
3. Do not automate Claude Desktop/Web through unsupported UI automation.
4. GitHub may prepare the next control packet, but a human starts/resumes the Claude Desktop/Web execution during this pilot.
5. Claude must not remain active merely to wait for Boss, ChatGPT, peers, approvals, or new commits.
6. When executable work is exhausted: persist state, commit, record the exact resume point, then stop.
7. Default execution continuity is **OLD SESSION FIRST**.
8. **NEW PROMPT != NEW SESSION**.
9. New Session is an exception and must preserve full continuity.
10. No Evidence = No Progress.
11. Never Skip Gate.
12. Boss is the sole Final Approver.

## Pilot Goal

Measure the real operating cost, token consumption, research quality, recovery behavior, and governance quality of Claude Desktop/Web before any API-based orchestration is authorized.

## Future Evolution — NOT AUTHORIZED IN THIS PILOT

Future versions may evaluate:

- GitHub webhook / event controller
- Node.js SMEsPlus Agent Orchestrator
- OpenAI Agent API
- Anthropic API
- Temporal durable workflow
- fully automated agent dispatch

These are design candidates only. They are **not authorized for current implementation**.

## Files

- `AI_EOS_NO_API_PILOT_CHARTER_2026_09_05.md`
- `EVENT_DRIVEN_NO_IDLE_STANDARD.md`
- `SESSION_CHECKPOINT_AUTO_RESUME_STANDARD.md`
- `TEMPLATES/CONTROL_PACKET_TEMPLATE.yaml`
- `TEMPLATES/AUTO_RESUME_STATE_TEMPLATE.yaml`

## Publication Model

Active engineering truth remains in GitHub.

After Boss Final Approval, approved corporate documents may be generated and published to Dropbox.

```text
GitHub Canonical Evidence
        ↓
Boss Final Approval
        ↓
Approved PDF / DOCX / Corporate Standard
        ↓
Dropbox Publication Repository
```
