# [SMEPLUS-26-09-11-DEVTOOL-VALIDATION-001]
## STEP03 — AI EOS Entry Point & Claude Dispatch Brief

Status: ACTIVE BRIEF / NOT FINAL FREEZE
Owner: SSA — Software & System Architect
Co-Owner: PSPA — Principal SaaS Platform Architect
Final Approver: Boss

## Executive Direction
The project is not currently using Make as an operational automation baseline. Prior Make exercises are learning/test evidence only.
STEP03 must therefore discover the actual capability gap and define where AI EOS should own execution control.

Core principle:
AI EOS = Execution / Orchestration / Control Plane.
Claude = Execution Worker / Coding Agent.
Make = NOT IN USE; reference/challenger only unless later evidence justifies a role.

## STEP03-A — Current Reality Inventory
Map what is actually working now: Prompt-driven work, GitHub, Jira, Claude/Claude Code, Figma, Playwright, evidence/gates, and manual handoffs.
Classify each edge as VERIFIED WORKING / WORKING WITH LIMITATIONS / DOCUMENTED NOT VERIFIED / PARTIAL / BLOCKED / NOT IN USE.

## STEP03-B — Manual Handoff & Automation Gap
Identify where a human currently has to copy a prompt, choose a destination, start Claude, watch execution, detect failure, retry, collect result, update Jira/GitHub, and preserve evidence.
These manual transitions are candidate AI EOS responsibilities.

## STEP03-C — Target Capability Contract
Define only capabilities SMEsPlus needs: unattended execution, deterministic dispatch, isolated workspace/branch, permission boundary, time/cost budget, timeout, retry/resume, status/heartbeat, evidence capture, test handoff, and human/Boss gates.
Unused features have zero selection value.

## STEP03-D — AI EOS Minimum Vertical Slice
Start AI EOS with a narrow controlled path:
Controlled Prompt -> AI EOS Intake -> Execution Job -> Claude Dispatch Adapter -> isolated Claude execution -> result/status collection -> evidence package -> human/gate handoff.
Do not start with a full multi-agent platform.

Minimum Execution Job fields:
job_id, session_id, prompt_ref, prompt_hash, task_type, target_agent, repository, branch/worktree, allowed_tools, prohibited_actions, time_budget, cost_budget, timeout, retry_policy, evidence_path, gate_state, owner, reviewer.

## STEP03-E — Claude Dispatch Boundary
AI EOS owns job state, routing, permissions, retry, timeout, evidence and lifecycle.
Claude owns only the assigned execution task within the supplied constraints.
Claude must not become the authoritative workflow state store, final approver, production release authority, or hidden orchestrator.

Reference flow:
Prompt -> AI EOS Job -> Dispatch Claude -> Claude Executes -> status/result -> AI EOS -> tests/evidence -> independent review -> Gate.

## STEP03-F — Expansion After Proof
After Claude Dispatch is proven, add adapters only where needed: frontend agent, backend specialist, test agent, review agent, Jira/GitHub connectors, Figma handoff, notification/integration services, or Make/n8n if a material gap remains.
Every new component must close a measured project gap.

## Why Start With Claude Dispatch
1. Prompt-driven execution is already the real project operating pattern.
2. Claude/Claude Code is already used as an engineering executor, so Dispatch creates immediate measurable value.
3. The largest automation gap is between approved Prompt and controlled unattended execution, not lack of features.
4. Keeping orchestration in AI EOS prevents vendor/model lock-in: Claude can later be replaced or supplemented without changing the project control plane.
5. A narrow vertical slice can prove state, permissions, retry, evidence, cost and human-gate behavior before building a larger AI platform.
6. Backend and frontend can later use different executors while sharing the same AI EOS job contract.

## Non-Negotiable Controls
No Evidence = No Progress.
No Gate skipping.
AI EOS must not silently approve, merge, release or deploy Production.
Agent failure must be visible and recoverable.
Prompt/hash/input/output/status/evidence lineage must be traceable.
Boss remains the sole Final Approver.
