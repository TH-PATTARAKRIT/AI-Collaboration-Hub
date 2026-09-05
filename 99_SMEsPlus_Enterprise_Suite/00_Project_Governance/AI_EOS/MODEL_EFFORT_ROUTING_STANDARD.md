# MODEL_EFFORT_ROUTING_STANDARD.md

Version: Pilot v0.1
Status: BOSS APPROVED PILOT CONTROL
Effective Date: 2026-09-05
Scope: SMEsPlus AI-EOS No-API Pilot

## Constraint

- NO OpenAI API.
- NO Anthropic API.
- Claude execution uses Claude Desktop or Claude Web only during the pilot.
- GitHub remains the canonical control/evidence backbone.
- Model/effort must be selected to preserve research quality while avoiding unnecessary usage consumption.

## Core Rule

Use the LOWEST model/effort tier that can safely satisfy the evidence and decision class.
Escalate only when a material trigger exists.
Do not use maximum effort as a blanket default.

## Work Classes

### Class A — Mechanical / Deterministic Control Work
Examples: manifest refresh, SHA/register update, checkpoint update, file inventory, formatting, already-defined delta ingestion, exact-count reconciliation with no semantic dispute.

Recommended: Claude Sonnet 5 — MEDIUM.
Escalate to Sonnet 5 HIGH only if the evidence population/tooling is ambiguous.

### Class B — Forensic Evidence Work
Examples: source/database/runtime tracing, denominator repair, version-identity checks, negative-claim verification, live-vs-latent classification.

Recommended: Claude Sonnet 5 — HIGH or Claude Opus 5 — MEDIUM.
Use Opus 5 MEDIUM when cross-file reasoning or contradictory evidence is material.

### Class C — Cross-Process / Architecture / Veto Work
Examples: P11 reconciliation, cross-process contradiction, scope-boundary adjudication, AAS+ veto, Boss-decision package preparation, accounting architecture implications.

Recommended: Claude Opus 5 — HIGH.

### Class D — Exceptional Irreducible Critical Work
Examples: a small bounded set of unresolved Boss-level decisions where Class C leaves materially competing interpretations after evidence is complete.

Recommended: Claude Opus 5 — XHIGH or MAX for ONE bounded pass only.
Return to HIGH/MEDIUM immediately after the bounded critical task.
MAX is not a default operating mode.

## P01–P10 Default

- Continuation / peer-delta / register refresh: Sonnet 5 MEDIUM.
- New forensic contradiction / denominator / source↔DB mismatch: Sonnet 5 HIGH.
- Material accounting architecture or veto implication: Opus 5 MEDIUM or HIGH depending on severity.
- Do not keep Opus 5 HIGH running for purely mechanical checkpoint work.

## P11 Default

P11 is the Central Core Reconciliation process.

Default for semantic reconciliation: Opus 5 HIGH.

Use Sonnet 5 MEDIUM for mechanical peer intake, manifest/register refresh, and already-decided formatting/update work when the UI/workflow permits model switching without losing the logical Old Session.

Use Opus 5 XHIGH/MAX only when:
1. evidence population is complete;
2. the unresolved item is Boss-level/material;
3. HIGH has left materially competing interpretations;
4. the task is bounded to a named decision/contradiction;
5. the agent commits and stops immediately after the bounded pass.

## Event-Driven Token Economy

Usage reduction must come from:
- Old Session continuity;
- checkpointing;
- auto-resume state;
- material-delta processing;
- peer last-consumed SHA;
- event-driven stop;
- no idle waiting;
- model/effort routing.

Usage reduction MUST NOT come from:
- skipping evidence;
- shrinking denominators;
- bypassing AAS-03/AAS+/PMO;
- skipping gates;
- premature closure.

## Escalation Triggers

Escalate one tier when any of the following is material:
- denominator cannot be established;
- evidence sources contradict;
- source and deployed database/runtime disagree;
- a prior FACT VERIFIED finding is overturned;
- a decision-authority boundary is implicated;
- AAS+ veto is opened/strengthened;
- Boss decision package changes materially;
- accounting sign/period/scope semantics reverse.

## De-escalation Triggers

Return to a lower tier when the remaining work is:
- deterministic;
- mechanical;
- already decided;
- register/manifest maintenance;
- checkpoint publication;
- exact delta ingestion with no semantic dispute.

## No-Idle Rule

When currently executable work is exhausted:
COMMIT → UPDATE CHECKPOINT → UPDATE AUTO_RESUME_STATE → RECORD NEXT EVENT → STOP.
Do not remain active waiting for Boss, peers, GitHub changes, permissions, or external evidence.

## Evidence Rule

No Evidence = No Progress.
Never Skip Gate.
Boss = Sole Final Approver.
