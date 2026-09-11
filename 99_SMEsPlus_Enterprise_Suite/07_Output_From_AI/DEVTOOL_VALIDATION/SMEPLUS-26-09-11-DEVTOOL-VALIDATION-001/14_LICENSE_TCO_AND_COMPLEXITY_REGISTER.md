# [SMEPLUS-26-09-11-DEVTOOL-VALIDATION-001]
## License, TCO & Operational Complexity Register

Status: RESEARCH BASELINE / PRICES SNAPSHOT 2026-09-11 WHERE LISTED
Owner: SSA
SaaS Cost Veto: PSPA
Final Approver: Boss

## Economic Rule
SMEsPlus targets Thai SMEs. The architecture must not load avoidable per-tenant/per-company runtime license cost into customer pricing.

`Low license price != Low TCO`.
`Paid development tool != Bad economics`.

Build-time tools can be paid when they materially reduce engineering time, defects, risk or time-to-market. Runtime/core tools are challenged more strictly because their costs may grow with tenants, companies, users, requests, storage or HA replicas.

## Cost Classes
| Class | Scaling Driver | Decision Rule |
|---|---|---|
| BUILD-TIME | engineer/designer seat, AI usage | Pay when measurable productivity/quality ROI exists |
| CONTROL/PMO | internal seat, CI minutes, storage, automation executions | Optimize but do not compromise evidence/governance |
| RUNTIME CORE | VM/CPU/RAM/DB/storage/queue/cache/egress/backup | Prefer open/free license; measure infrastructure and operations |
| TENANT-MULTIPLIER SERVICE | per user/tenant/request/action/GB/API call | Strong veto unless customer value justifies multiplier |
| OPTIONAL SPECIALIST | occasional test/review/design use | Prefer on-demand/free/self-hosted where practical |

## Current Paid/Commercial Snapshot
### Figma
Official pricing snapshot:
- Starter: Free.
- Professional: Full $16/month; Dev $12/month; Collab $3/month (monthly display at research time).
- Organization: Full $55/month; Dev $25/month; Collab $5/month, annual billing.
- Enterprise: Full $90/month; Dev $35/month; Collab $5/month, annual billing.
- Code Connect requires Organization or Enterprise with Full/Dev seat.

TCO disposition: `PAY SELECTIVELY`. Full/Dev seats scale with design/development team, not customer tenant count. Do not buy Organization/Enterprise merely for Code Connect before ROI is proven.

### Jira
Official snapshot:
- Free: up to 10 users, 150 automation steps/subscription/month.
- Standard: $7.91/user/month; 400 automation steps/user/month.
- Premium: $14.54/user/month; 1,000 automation steps/user/month and customizable approvals.

TCO disposition: `INTERNAL TEAM COST`. Retain if traceability/evidence value remains strong; do not expose every customer user as a Jira paid seat.

### GitHub
Official snapshot:
- Free: $0; 2,000 GitHub Actions minutes/month for private-repo hosted runners.
- Team: $4/user/month; 3,000 Actions minutes/month.
- Enterprise: $21/user/month; 50,000 Actions minutes/month.
- Self-hosted Actions runner execution itself is not billed by GitHub Actions, but SMEsPlus bears runner infrastructure/operations cost.

TCO disposition: `STRONG INTERNAL PLATFORM ECONOMICS`, subject to repository/security feature requirements and CI usage.

### GitHub Copilot
Official organization snapshot:
- Business: $19/user/month, 1,900 AI credits/user.
- Enterprise: $39/user/month, 3,900 AI credits/user.

TCO disposition: `BUILD-TIME CHALLENGER`. Compare against Claude/Codex/Junie/Cursor on cost-per-accepted-task, not seat price alone.

### Make
Official snapshot at 10,000-credit selection:
- Free: 1,000 credits/month.
- Core: $12/month for 10,000 credits.
- Pro: $21/month for 10,000 credits.
- Teams: $38/month for 10,000 credits.
- Enterprise: custom.
- Most module actions consume a credit; advanced AI-related actions may consume more.

TCO disposition: `NOT IN OPERATIONAL USE / OPTIONAL CONNECTOR`. Action-credit pricing is a workload multiplier. Do not make it AI EOS core without volume economics and failure/recovery evidence.

### n8n
Licensing disposition: `SPECIAL LEGAL/COMMERCIAL REVIEW` if SMEsPlus hosts/manages client workflows or credentials or embeds n8n. Official licensing guidance says those models may require Enterprise or Embed commercial licenses. Self-host availability must not be misread as unrestricted SaaS embedding rights.

## Open/Free Runtime Foundation Candidates
| Tool | License / Cost Character | Tenant Multiplier | Operations Complexity | Research Disposition |
|---|---|---:|---|---|
| Linux Debian 13 | open distribution | No license multiplier | Low-Medium | OS FINALIST |
| Ubuntu 26.04 LTS | open distribution; optional paid Pro | No mandatory license multiplier | Low-Medium | OS FINALIST |
| Node.js 24 LTS | permissive/MIT-dominant distribution | None | Low | PREFERRED BASELINE CANDIDATE |
| PostgreSQL 18 | PostgreSQL License, no fee | None | Medium | STRONG CORE CANDIDATE |
| Podman | open-source container engine | None | Low-Medium | PILOT |
| Caddy | Apache-2.0 | None | Low | PILOT |
| NGINX OSS | open-source | None | Low-Medium | CHALLENGER |
| Valkey | BSD-3-Clause | None | Medium | PILOT |
| RabbitMQ | open-source core | None | Medium-High | MESSAGING FINALIST |
| NATS | open-source core | None | Medium | MESSAGING FINALIST |
| OpenTofu | MPL-2.0 | None | Medium | IaC PILOT |
| Ansible | open-source | None | Medium | CONFIG/DEPLOY PILOT |
| SeaweedFS | Apache-2.0 | None | Medium-High | OBJECT STORAGE PILOT |
| Ceph | open-source | None | High | HOLD UNTIL SCALE |
| pgBackRest | MIT | None | Medium | STRONG BACKUP CANDIDATE |
| OpenTelemetry | Apache-2.0 | None | Medium | STRONG INSTRUMENTATION CANDIDATE |
| Prometheus | Apache-2.0 | None | Medium | STRONG OPS METRICS CANDIDATE |
| Loki | AGPL ecosystem / security config needed | None | Medium-High | PILOT WITH SECURITY GATE |
| Grafana OSS | AGPL | None | Medium | PILOT |
| Playwright | Apache-2.0 | None | Low-Medium | STRONG TEST CANDIDATE |
| Pact JS | MIT | None | Low-Medium | SPECIALIST |
| k6 OSS | open-source | None | Low-Medium | STRONG PERF CANDIDATE |
| Structurizr core/tools | Apache-2.0; prebuilt server has separate licensing considerations | Internal use | Low-Medium | ARCHITECTURE PILOT |
| bpmn.io toolkit | permissive-style with mandatory visible watermark condition | Internal use | Low | BPMN PILOT |
| Hatchet OSS | MIT | None | Medium | AI EOS ENGINE PILOT |
| Temporal OSS | MIT core ecosystem | None | Medium-High | AI EOS ENGINE CHALLENGER |

## TCO Scenario Model — Do Not Invent Workload
The canonical comparison must model at least:
- `S`: 50 tenants
- `M`: 200 tenants
- `L`: 1,000 tenants
- `XL`: 5,000 tenants

Until workload evidence exists, calculate with formulas rather than fake numbers:

`Monthly Runtime TCO(N) = Compute(N) + DB(N) + Cache/Queue(N) + ObjectStorage(N) + Egress(N) + Backup/DR(N) + Observability(N) + Security(N) + OperationsLabor(N) + PaidRuntimeLicenses(N)`

`Cost per Active Tenant = Monthly Runtime TCO / Active Tenants`

`Automation Cost = Fixed Platform Cost + Executions × ActionsPerExecution × UnitCost + AI/API Variable Cost`

`AI Engineering Cost per Accepted Task = Seat/API Cost + CI Cost + Human Review Time + Retry/Rework Cost`

## Mandatory Scale Questions for Every Runtime Candidate
1. Does license cost increase by tenant, company, user, server/core, request, workflow action or storage?
2. What infrastructure is required for minimum safe HA?
3. What does backup/restore add?
4. What is the egress cost if data is moved out?
5. What is the operational labor/skill burden?
6. Can SMEsPlus migrate away without proprietary data lock-in?
7. What is the cost of isolation for Standard cell vs Enterprise dedicated tenant?
8. Can the same open core semantics run in both deployment models?

## Complexity Budget
Do not deploy a Ferrari stack on a rough road.
- Kubernetes: HOLD until a measured orchestration/scale/HA trigger exists.
- Ceph: HOLD until object/block/file consolidation or scale justifies a cluster.
- OpenBao: HOLD until dynamic/central secret issuance is required.
- Figma Organization/Enterprise: HOLD unless Code Connect/admin/security ROI is demonstrated.
- Make/n8n paid embedding: HOLD unless integration gap and unit economics are demonstrated.

## Final Economic Principle
Select the `lowest sustainable TCO` that still satisfies correctness, security, tenant isolation, reliability, recoverability, maintainability and evidence requirements.
