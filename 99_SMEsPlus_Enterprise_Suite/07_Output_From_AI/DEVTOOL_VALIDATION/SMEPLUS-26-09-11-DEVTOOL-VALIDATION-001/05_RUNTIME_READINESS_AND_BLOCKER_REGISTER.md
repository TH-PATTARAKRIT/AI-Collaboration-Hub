# 05_RUNTIME_READINESS_AND_BLOCKER_REGISTER

Session: SMEPLUS-26-09-11-DEVTOOL-VALIDATION-001
Status: CLI SMOKE VERIFIED / AUTHENTICATED COMPARATIVE BENCHMARK INCOMPLETE

## Neutral Runtime Proof — GitHub Actions
Workflow: `.github/workflows/devtool-cli-smoke.yml`
Run ID: 34613164004
Commit: 36bac0ab5886dd39491c294ab82164996f6e5c30
Runner: Ubuntu 24.04 / ubuntu-24.04 image
Permissions: contents:read; metadata:read.
No candidate API key was required for this smoke test.

| Candidate | Install | Version/Help | Verified Version | CLI Disposition |
|---|---|---|---|---|
| Claude Code | PASS | PASS | 2.1.268 | CLI AVAILABLE |
| OpenAI Codex | PASS | PASS | 0.154.0 | CLI AVAILABLE |
| Cursor Agent | PASS | PASS | 2026.09.10-fd3934a | CLI AVAILABLE |
| JetBrains Junie | PASS | PASS | 26.9.7 (3110.7) | CLI AVAILABLE |

Artifacts:
- Claude 10268429901
- Codex 10269064299
- Cursor 10268949605
- Junie 10269555706

## GitHub Actions Credential Readiness
Controlled presence-only workflow found the standard names ANTHROPIC_API_KEY, OPENAI_API_KEY, CURSOR_API_KEY and JUNIE_API_KEY absent in the checked repository Actions context. Values were not printed or persisted. This finding is scoped to those names/context only.

## Authorized Remote Workstation Runtime
Device: authorized SMEsPlus development workstation. Sensitive user/account identifiers are intentionally excluded from this evidence record.

### Claude Code
- CLI version observed: 2.1.263.
- Authentication status: authenticated via supported account mechanism.
- B01 executed in detached read-only worktree with write/edit/bash mutation disallowed.
- Inference did not start: provider returned HTTP 400 `Credit balance is too low`.
- Token use: zero for the failed inference attempt; worktree remained clean.
Disposition: AUTH/BILLING BLOCKER — NOT SCORED FOR QUALITY.

### OpenAI Codex
- CLI version observed: 0.154.0 through `npx -y @openai/codex`.
- Authentication status: authenticated via supported ChatGPT login.
- B01 executed with read-only sandbox, ephemeral session and frozen prompt/snapshot.
- Result produced; worktree remained clean.
- Recorded usage: input 289081 tokens, cached input 234880, output 3670, reasoning output 129.
Disposition: B01 RESULT AVAILABLE — PENDING INDEPENDENT CLAIM REVIEW; one scenario is insufficient for winner selection.

### Cursor Agent
- CLI version observed: 2026.09.10-fd3934a.
- `agent status`: not logged in.
Disposition: AUTH BLOCKED — NOT SCORED.

### JetBrains Junie
- Installed on authorized macOS workstation from JetBrains official installer.
- CLI version observed: 26.9.7 (3110.7).
- Help output confirms interactive and non-interactive task modes, JSON/text outputs, project targeting, gateway/headless worker, model/provider selection, MCP/config/skills/agent locations and explicit authentication inputs.
- Controlled non-interactive smoke in an empty temporary project disabled default project config/MCP/skill/agent/command loading and asked for no file changes.
- Result before inference: `Cannot find authorization. Please authenticate before running Junie.`
Disposition: CLI AVAILABLE / AUTH BLOCKED — NOT SCORED.

## Comparative Control
Claude, Cursor and Junie authentication/account dependencies remain unresolved. Codex having the only current B01 result does NOT make Codex the winner.
A fair coding-agent comparison requires the same frozen SMEsPlus-derived clean-room fixture, acceptance oracle, time/cost/permission budget and independent grading.

## Benchmark Fairness Requirement
Two tracks are required where tool-specific repository instructions could create home-field advantage:
- Track N — Neutral Harness: canonical hashed instructions, no candidate-specific skills/config/context beyond equivalent required inputs.
- Track I — Native Integration: candidate-specific supported project instructions/integrations allowed and measured as part of harness value.
Model score and agent-harness score must be reported separately where a host can use multiple model providers.

## Governance Disposition
CLI runtime proof is verified for Claude Code, Codex, Cursor and Junie.
Authenticated comparative quality proof is INCOMPLETE.
No universal AI-coding winner may be declared.
Unresolved auth/billing blockers do not stop non-auth STATE-by-STATE research.
Boss-only action is deferred to Final Gate unless comparative execution is still required for a final selection.

No Evidence = No Progress.
