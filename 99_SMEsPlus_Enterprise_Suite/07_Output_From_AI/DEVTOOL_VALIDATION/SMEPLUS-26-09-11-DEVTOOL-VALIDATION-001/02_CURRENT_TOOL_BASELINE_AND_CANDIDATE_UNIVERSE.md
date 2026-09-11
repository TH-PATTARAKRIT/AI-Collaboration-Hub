# 02_CURRENT_TOOL_BASELINE_AND_CANDIDATE_UNIVERSE

Session: SMEPLUS-26-09-11-DEVTOOL-VALIDATION-001
Status: ACTIVE — NOT FINAL FREEZE

## Current/Historical Rule
Prior SMEsPlus choices are learning/current/historical evidence only. They do not confer automatic PASS or canonical ownership.

Explicit correction from Boss:
- Make = NOT IN OPERATIONAL USE / LEARNING & TEST REFERENCE ONLY.
- Figma, Lovable and other previously chosen tools must be re-proven against current SMEsPlus missions.
- VS Code remains REMOVED / NOT IN USE / EXCLUDED unless Boss reopens it.

## Candidate Universe — Expanded by Mission
| Mission | Candidate(s) | Current Disposition |
|---|---|---|
| Architecture / Research / Review | ChatGPT; Claude; structured docs-as-code | RE-PROVE BY MISSION |
| Architecture modeling | Structurizr; Mermaid; PlantUML | ADMITTED FOR RESEARCH |
| Process / BPMN | bpmn.io and compatible BPMN tooling | ADMITTED FOR RESEARCH |
| API / Event contract | OpenAPI/Swagger; AsyncAPI | ADMITTED FOR RESEARCH |
| Functional design / requirements | GitHub Markdown/YAML + Jira + AI review; specialist modeling tools where gap exists | ADMITTED / BENCHMARK BY STEP |
| UI/UX | Figma | HISTORICAL STRONG CANDIDATE / RE-PROVE |
| Design-to-code / prototype | Figma Dev Mode/MCP; Lovable; coding agents | MISSION-SPECIFIC CHALLENGERS |
| AI coding | Claude Code; OpenAI Codex; Cursor; JetBrains Junie; GitHub Copilot; Factory Droid | ACTIVE COMPARATIVE SET |
| Source / PR / CI | GitHub; GitHub Actions | STRONG CORE CANDIDATE |
| PMO / traceability | Jira + GitHub evidence links | STRONG CORE CANDIDATE |
| E2E / browser evidence | Playwright | STRONG CORE CANDIDATE / RE-PROVE |
| Integration testing | Testcontainers | ADMITTED |
| Contract testing | Pact | ADMITTED FOR APPLICABLE APIs |
| Performance/load | Grafana k6 | ADMITTED |
| Security dynamic testing | OWASP ZAP | ADMITTED |
| Policy-as-code | Open Policy Agent | ADMITTED |
| Secret file/GitOps control | SOPS + age/KMS | ADMITTED |
| Central/dynamic secrets | OpenBao | CONDITIONAL CHALLENGER; complexity proof required |
| Runtime IAM | Keycloak | CONDITIONAL CHALLENGER; operations/tenant model proof required |
| AI/workflow durable orchestration | Temporal; Hatchet; Trigger.dev | ACTIVE RESEARCH SET |
| Job queue | BullMQ | SPECIALIST CHALLENGER; not equivalent to durable workflow engine |
| Integration automation | Make; n8n; direct API/webhook/native automation | REFERENCE/CHALLENGER — NO INCUMBENT WINNER |
| Server OS | Debian 13; Ubuntu 26.04 LTS | FINALIST RESEARCH SET |
| Runtime | Node.js 24 LTS baseline candidate; Node 26 Current for future evaluation | NODE 24 LTS PREFERRED RESEARCH BASELINE |
| Database | PostgreSQL 18.x | STRONG OPEN-LICENSE CANDIDATE |
| Messaging | NATS; RabbitMQ | MISSION BENCHMARK REQUIRED |
| Cache | Valkey | OPEN-LICENSE CANDIDATE |
| Reverse proxy / TLS | Caddy; NGINX | MISSION BENCHMARK REQUIRED |
| Object storage | SeaweedFS; Ceph RGW; managed S3-compatible service where economics justify | BENCHMARK / TCO REQUIRED |
| PostgreSQL backup | pgBackRest | STRONG CANDIDATE; restore drill mandatory |
| Telemetry | OpenTelemetry | STRONG INSTRUMENTATION CANDIDATE |
| Metrics/alerting | Prometheus + Alertmanager | STRONG CANDIDATE; not exact billing source |
| Logs | Loki | CONDITIONAL; auth/tenant enforcement mandatory |
| Dashboard | Grafana OSS | STRONG CANDIDATE subject to license/ops review |
| Knowledge portal | GitHub canonical docs + Docusaurus derived view | ADMITTED |
| Semantic retrieval | PostgreSQL + pgvector if material need proven | OPTIONAL / AVOID PREMATURE EXTRA DB |
| Current context | GitHub machine-readable context + Jira active work; later AI EOS state store | DESIGN TARGET, NOT THIRD-PARTY TOOL WINNER |

## Runtime Coding-Agent Evidence
Neutral GitHub Actions CLI smoke has already verified install/version/help for Claude Code, Codex, Cursor and Junie. Remote authorized workstation checks further established:
- Claude CLI available/authenticated, but B01 inference blocked by account credit balance; NOT SCORED.
- Codex CLI available through npx and authenticated via supported user login; B01 read-only project benchmark produced a result with clean worktree; independent review still required.
- Cursor Agent installed; authentication absent; benchmark blocked; NOT SCORED.
- Junie 26.9.7 (3110.7) installed successfully; non-interactive auth smoke reports no authorization; benchmark blocked; NOT SCORED.

Therefore no universal AI-coding winner is declared.

## Candidate Admission Rule
Admit a new tool only when it closes a material STATE/STEP mission gap or materially improves security, governance, reliability, portability, TCO or maintainability. Do not add tools merely because they are popular or feature-rich.

## Selection Rule
Mission Fit + Constraint Fit + Runtime Evidence + Governance Fit + Sustainable TCO.
Existing != Best. Paid != Better. Free != Better. New != Improvement.
No Evidence = No Progress.
