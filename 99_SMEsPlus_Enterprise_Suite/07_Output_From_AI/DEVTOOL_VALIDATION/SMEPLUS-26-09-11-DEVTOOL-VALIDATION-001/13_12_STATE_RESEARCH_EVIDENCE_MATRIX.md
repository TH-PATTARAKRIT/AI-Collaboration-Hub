# [SMEPLUS-26-09-11-DEVTOOL-VALIDATION-001]
## 12-STATE Deep Research Evidence Matrix

Status: RESEARCH COMPLETE FOR DOCUMENT/CAPABILITY SCREENING; RUNTIME PROOF VARIES BY TOOL
Owners: SSA + PSPA
Final Approver: Boss
Clean Room: 100%

## Research Method
Every recommendation is mission-specific. Vendor documentation proves advertised/current capability, not SMEsPlus runtime fitness. Repository evidence proves current SMEsPlus mission/control, not that a current tool is best. Runtime proof and TCO are separated from feature discovery.

Disposition vocabulary:
- `KEEP-CANDIDATE` — current/historical tool remains strong and should stay in comparative set.
- `SUPPLEMENT-CANDIDATE` — closes a material gap without replacing the primary tool.
- `REPLACE-CANDIDATE` — materially challenges a current/historical choice.
- `PILOT` — fit appears strong but SMEsPlus runtime proof is required.
- `HOLD` — insufficient proof or unresolved economic/security/operational dependency.
- `REJECT-FOR-MISSION` — poor fit for this specific mission; may still fit elsewhere.

---

## STATE01 — Identity
### Proven Mission
Project identity, product vision, scope/exclusions, role/authority/RACI, AI-support boundary, evidence ownership and source-of-truth.

### Research Finding
Do not buy a standalone identity-governance suite for project metadata when GitHub + structured files + Jira already provide auditable ownership and change lineage. Runtime customer/user IAM is a different mission and should not be conflated with project-role identity.

### Tool Mapping
- GitHub — `KEEP-CANDIDATE` for canonical project identity, role definitions, versioned registries and evidence pointers.
- Jira — `KEEP-CANDIDATE` for active owner/assignee/status/work accountability.
- Keycloak — `PILOT` for application/runtime IAM only: OIDC/OAuth2/SAML, service accounts, federation and MFA capabilities make it a serious open-source candidate, but it adds an always-on identity service and operations burden.
- SOPS — `SUPPLEMENT-CANDIDATE` for encrypted configuration/secrets stored with GitOps; keep project identity separate from secret material.

### Tool Principle
Project identity = Git evidence. Runtime identity = dedicated IAM only if application/security requirements justify it.

---

## STATE02 — Governance
### Proven Mission / STEP Coverage
Step 01–07 cover governance inventory, authority conflict, RACI, ownerless execution control, governance index, gate crosswalk and evidence/approval standard.

### Research Finding
Governance should remain `docs-as-code + machine-enforceable checks`, not become a new expensive platform.

### Tool Mapping
- GitHub + protected PR/change lineage — `KEEP-CANDIDATE` canonical governance evidence.
- Jira — `KEEP-CANDIDATE` active decisions/work items, but not sole source of policy truth.
- GitHub Actions — `SUPPLEMENT-CANDIDATE` for automatic policy/evidence checks.
- Open Policy Agent (OPA) — `PILOT` for policy-as-code where decisions need deterministic machine evaluation.
- SOPS — `SUPPLEMENT-CANDIDATE` for secret/config protection.
- OpenBao — `HOLD/PILOT ONLY IF NEEDED` for dynamic/central secrets; operational complexity is not justified until dynamic credential rotation or centralized secret issuance is a proven requirement.

### Economic Position
Prefer repository-native controls first. Do not add a paid GRC platform unless a compliance requirement proves a material gap.

---

## STATE03 — Architecture
### Proven STEP Coverage
STEP0301, STEP0302 + substeps, STEP0303 + R1; Boss identifies STEP0304 as later deep-research parent, but formal title remains unresolved in current repository search.

### Research Finding
Architecture needs text/model artifacts that are diffable, AI-readable and reviewable. Static drawing tools alone are insufficient as canonical architecture truth.

### Tool Mapping
- GitHub Markdown/YAML/JSON + ADR — `KEEP-CANDIDATE` canonical architecture evidence.
- Structurizr DSL/C4 — `PILOT` for models-as-code; official documentation explicitly positions it as version-control and AI friendly. Commands are free; prebuilt server use has separate licensing considerations.
- Mermaid — `KEEP/SUPPLEMENT` for lightweight diagrams embedded in Markdown.
- PlantUML — `OPTIONAL` for teams needing richer text diagrams; avoid duplication with Structurizr/Mermaid without mission need.
- bpmn.io — `SUPPLEMENT-CANDIDATE` for BPMN/DMN/form modeling; free-use license has a required visible bpmn.io watermark in embedded rendered diagrams.
- OpenAPI/Swagger tooling — `KEEP/PILOT` for synchronous API contracts.
- AsyncAPI CLI/Studio — `SUPPLEMENT-CANDIDATE` for event contracts; current CLI supports validate, diff, generate and CI-friendly diagnostics.

### Clean Room Position
Architecture models must describe SMEsPlus-owned semantics and public standards. No proprietary ERP schema/workflow/ORM may be imported into model-as-code artifacts.

---

## STATE04 — Functional
### Proven STEP Coverage
STEP0401 and substep evidence are proven; authoritative later STEP naming is not fully resolved in this pass.

### Research Finding
Functional Design must stay traceable from research/business rule to acceptance criteria. A heavyweight functional-modeling suite is not justified unless the Markdown/YAML/BPMN approach fails a controlled pilot.

### Tool Mapping
- GitHub Markdown/YAML + canonical FDS templates — `KEEP-CANDIDATE` for functional specification and business rules.
- Jira — `KEEP-CANDIDATE` for requirement/work traceability, not canonical design truth.
- AI research/review agents — `PILOT BY ROLE`; generated FDS is draft until independently reviewed.
- bpmn.io — `SUPPLEMENT-CANDIDATE` where BPMN materially improves process clarity.
- OpenAPI/AsyncAPI — `SUPPLEMENT-CANDIDATE` when functional handoff reaches interface contracts.

### Required Proof
FDS completeness, contradiction rate, traceability to source evidence, acceptance-criteria quality, Thai localization and clean-room provenance.

---

## STATE05 — UX/UI
### Proven Mission
UX / interaction / user journey; repository policy currently routes this mission to Figma and the master template defines a Design-to-Code Contract artifact family.

### Research Finding
Figma remains a strong incumbent candidate but must be selected for what SMEsPlus actually needs. Current official pricing provides a free Starter tier, Professional Full/Dev seats and higher Organization/Enterprise tiers. Advanced Dev Mode/MCP is available on paid tiers; Code Connect specifically requires Organization or Enterprise Full/Dev seats.

### Tool Mapping
- Figma Design — `KEEP-CANDIDATE` as design authority after workflow re-proof.
- Figma Dev Mode/MCP — `PILOT` for developer/AI handoff; use only for roles that need it rather than buying unnecessary seats.
- Figma Code Connect — `HOLD UNTIL ROI PROVEN` because it requires Organization/Enterprise and therefore adds significant per-seat cost.
- Lovable — `SUPPLEMENT/PROTOTYPE CANDIDATE`, not canonical implementation owner. Official docs state it cannot import an existing GitHub repository; it syncs Lovable-created projects to GitHub and depends heavily on the default branch/repository identity. This is a poor fit as the primary coding layer for an existing controlled SMEsPlus repository but can still be useful for greenfield UX/prototype exploration.
- Storybook/visual component tooling — `PILOT` for component catalog and design-system verification downstream.

### Economic Position
Pay Figma where collaboration/handoff benefit is material; do not assign paid Dev/Full seats to users who only need viewer/comment access.

---

## STATE06 — Development
### Proven Mission
Implementation / Engineering from approved design/FDS only.

### Platform Baseline Research
- Node.js 24 LTS — `PREFERRED RESEARCH BASELINE`; Node.js 26 is Current as of 2026-09, while Node 24 remains LTS. Production should prefer the supported LTS line unless a specific Node 26 feature is required and proven.
- PostgreSQL 18.x — `STRONG BASELINE CANDIDATE`; current 18.6 is supported through 2030-11-14 and PostgreSQL uses a liberal no-fee open-source license.
- TypeScript — `STRONG LANGUAGE CANDIDATE` for clean-room Node.js implementation.
- Fastify — `PILOT` for backend HTTP/API layer; choose against actual performance/plugin/validation needs rather than framework popularity.
- React + Vite — `PILOT` for ERP application frontend where client-side SaaS UX dominates. SSR/framework additions require a proven business need.

### AI Coding Agent Runtime Evidence
- Claude Code — CLI runtime proven; authenticated B01 blocked by account credit balance; `NOT SCORED`.
- OpenAI Codex — CLI/authenticated runtime proven; B01 result exists with clean read-only worktree; independent claim review pending; `PILOT / NO WINNER`.
- Cursor — CLI installed/proven; not logged in; `AUTH BLOCKED / NOT SCORED`.
- JetBrains Junie — 26.9.7 CLI installed/proven; non-interactive/headless/gateway capabilities visible; auth absent; `AUTH BLOCKED / NOT SCORED`.
- GitHub Copilot — `MATERIAL CHALLENGER`; GitHub-native agent/CLI/code-review and organization policy controls merit a later same-task pilot, but per-seat plus AI-credit economics must be measured.

### Decision
No universal AI coding winner. Keep the executor layer pluggable. Separate model quality from agent-harness quality.

---

## STATE07 — Testing
### Proven Mission
Unit/integration/E2E/FAT/UAT/defect/screenshot evidence. Evidence cannot be closed by assertion.

### Tool Mapping
- Playwright — `KEEP-CANDIDATE` primary browser E2E/runtime evidence. Official CI guidance supports repeatable browser execution; Apache-2.0 licensed.
- Testcontainers — `SUPPLEMENT-CANDIDATE` for real PostgreSQL/cache/queue integration tests rather than excessive mocks.
- Pact — `SUPPLEMENT-CANDIDATE` for applicable consumer-driven contract boundaries; MIT licensed. Do not use it as a substitute for full provider functional tests.
- Grafana k6 — `SUPPLEMENT-CANDIDATE` for load/performance. Thresholds produce deterministic pass/fail and non-zero CI status on breach.
- OWASP ZAP — `SUPPLEMENT-CANDIDATE` for automated dynamic security testing.
- GitHub Actions/artifacts/attestations — `SUPPLEMENT-CANDIDATE` for immutable-ish build/test provenance and evidence packaging.

### Required Proof
Test determinism, false-positive/flake rate, evidence retention, CI cost, Thai/browser coverage and runtime isolation.

---

## STATE08 — AI Execution / AI EOS
### Proven Mission
Prompt guard, scope/hallucination control, output log, reviewer evidence, dispatch/orchestration in the future AI EOS.

### Research Finding
Make/n8n are not the center of the design. The mission is reliable, recoverable execution across long-running AI/tool jobs with explicit state, retry, timeout, budget, human gates and evidence.

### Candidate Mapping
- SMEsPlus AI EOS — `TARGET CONTROL PLANE`; project-owned policies/state/contracts must remain vendor-independent.
- Hatchet — `FIRST PILOT CANDIDATE`: open-source MIT, TypeScript support, self-host/cloud, Postgres durability, queues/retries/events/webhooks/monitoring and durable tasks with checkpoint/replay. It matches SMEsPlus Node/Postgres economics but still requires runtime proof.
- Temporal — `MAJOR CHALLENGER`: mature durable workflow semantics, automatic activity retry and TypeScript SDK; strong fit for correctness/replay but operational complexity must be compared with Hatchet.
- Trigger.dev — `CHALLENGER` for developer-friendly background jobs; test if simpler road is sufficient.
- BullMQ — `SPECIALIST`, useful job queue but not equivalent to a full durable workflow/state system.
- Make — `REFERENCE/OPTIONAL CONNECTOR`; currently NOT operationally used. Current pricing is credit/action based, which can become a workflow-volume multiplier.
- n8n — `REFERENCE/OPTIONAL CONNECTOR`; license must be treated carefully if hosting client workflows/credentials or embedding the product, which may require commercial licensing.

### Decision Direction
Pilot durable workflow engines before selecting a no-code automation service as AI EOS core. Make/n8n may remain edge connectors only if they close a real integration gap.

---

## STATE09 — Infrastructure
### Proven Mission
Server/VM/container/database/backup/monitoring/security/capacity/DR.

### Tool Mapping
- Debian 13.6 — `OS FINALIST`; stable, full support to 2028-08, LTS to 2030-06.
- Ubuntu 26.04 LTS — `OS FINALIST`; standard security maintenance to 2031-05, optional extended support longer. Default-vs-Debian decision needs provider image/support/ops evidence.
- Podman + Quadlet/systemd — `PILOT/PREFERRED SIMPLE-RUNTIME CANDIDATE`; avoids premature Kubernetes complexity for bounded cells/private deployments.
- Kubernetes — `HOLD`; admit only at measured scale/HA/operational trigger, not because it is industry-popular.
- Caddy — `PILOT` reverse proxy/TLS candidate; supports load balancing and active/passive health checks with relatively simple config.
- NGINX — `CHALLENGER/FALLBACK` where ecosystem/ops evidence wins.
- PostgreSQL 18.x — `STRONG CORE CANDIDATE`.
- Valkey — `PILOT` open BSD cache/ephemeral data candidate.
- RabbitMQ quorum queues vs NATS — `MISSION BENCHMARK`; pick by delivery semantics, topology, ops and throughput evidence.
- OpenTofu — `PILOT` infrastructure-as-code; MPL-2.0.
- Ansible — `PILOT` host configuration/deployment automation; complements, not replaces, IaC state.
- SeaweedFS — `OBJECT-STORAGE PILOT`; S3/object/file capability and Apache-2.0 license; benchmark durability/backup/ops.
- Ceph — `HOLD FOR SCALE`; powerful object/block/file platform but higher cluster/operations complexity is likely poor early-road fit.
- Managed S3-compatible storage — `TCO CHALLENGER`; compare egress/retention/DR/support against self-hosting.
- pgBackRest — `STRONG BACKUP CANDIDATE`; free MIT PostgreSQL backup/restore tooling; mandatory restore/DR drill before selection.

---

## STATE10 — Production Operations
### Proven Mission
Incident/SLA/monitoring/change control, observability, backup/restore/DR, upgrade/rollback and runbook evidence.

### Tool Mapping
- OpenTelemetry — `STRONG INSTRUMENTATION CANDIDATE`; JS traces/metrics stable, logs still development, so do not overclaim a complete logging solution.
- Prometheus + Alertmanager — `STRONG OPS CANDIDATE`; use for operational metrics/alerts, not exact financial billing/metering.
- Loki — `PILOT WITH SECURITY GATE`; multi-tenant logs require an authentication proxy and controlled tenant-header handling because Loki itself does not provide built-in authentication.
- Grafana OSS — `PILOT` dashboard/observability UI subject to license/ops review.
- pgBackRest — `KEEP/PILOT` backup and recovery.
- GitHub Actions + Ansible/OpenTofu/Podman — `PILOT` controlled deploy path with protected environments and explicit Boss/production gates.

### Principle
No Kubernetes/large observability stack until operating evidence justifies it. Exact SaaS usage/billing events must come from application-owned immutable metering, not Prometheus sampling/scrape data.

---

## STATE11 — Knowledge Base
### Proven Mission
Reviewed knowledge only; completeness/version/owner/searchability; raw AI output is not approved knowledge.

### Tool Mapping
- GitHub Markdown/YAML/JSON — `KEEP-CANDIDATE` canonical knowledge/evidence source.
- Docusaurus — `SUPPLEMENT-CANDIDATE` read-friendly generated portal; never a second source of truth.
- PostgreSQL + pgvector — `OPTIONAL PILOT` for semantic retrieval only when corpus/search benchmarks prove material benefit. Avoid a new vector database before need is proven.
- AI summarization/indexing — `SUPPLEMENT`, but every derived summary needs source pointers/version/freshness.

### Economic Position
Reuse Git/Postgres before adding another paid KB/search platform.

---

## STATE12 — Current Context
### Proven Mission
Current State/STEP/session/status/blocker/next action/owner/evidence with no unsupported progress claims.

### Tool Mapping
- GitHub machine-readable `CURRENT_CONTEXT.md/json/yaml` generated from canonical registers — `PREFERRED DESIGN`.
- Jira — `SUPPLEMENT` for live execution issue/status/assignee.
- AI EOS state store — `FUTURE OWNER` for machine execution state after STATE08 architecture is proven.
- Slack/chat — `NOT SOURCE OF TRUTH`; notification/conversation only.

### Principle
Current Context should be generated from sources of truth, not manually copied into another paid tool.

---

## Cross-State Findings
1. The current toolchain should be modular by mission; no single vendor should own all 12 States.
2. GitHub is a strong cross-State evidence backbone but must not be mistaken for the owner of Functional/UX/AI orchestration semantics.
3. Jira is a strong PMO traceability layer but not the canonical design or code source.
4. Figma remains strongest for State-05 design authority, while its higher paid collaboration/Code Connect features must justify seat cost.
5. AI coding remains `HOLD FOR COMPARATIVE WINNER`; current Codex evidence is not enough to declare a winner.
6. AI EOS should first compare durable execution engines rather than assume Make/n8n as the core.
7. Runtime foundation can be largely open/free licensed: Linux, Node.js, PostgreSQL, Podman, Valkey, Caddy/NGINX, OpenTofu, Ansible, OpenTelemetry, Prometheus, Playwright, k6 and pgBackRest — but operational TCO still requires proof.
8. Avoid premature Kubernetes/Ceph/OpenBao complexity unless measured workload/security/HA needs trigger them.
9. Clean Room 100% applies to every AI/tool handoff, fixture and generated artifact.

## Evidence Sources — Primary/Official Research Set
Repository: SMEsPlus STATE Gate Matrix, State01 closure, State02 Step Status Register, State03 Step Register, State04 evidence/handoff, controlled carry-forward policy, master templates, KB rules.
External official/public: Figma pricing/Dev Mode/Code Connect; Lovable GitHub integration docs; Structurizr docs; bpmn.io license; AsyncAPI docs; Node.js release policy; PostgreSQL version/license; Playwright CI/license; Grafana k6 thresholds; Hatchet docs/repository; Temporal docs; Debian/Ubuntu lifecycle; Caddy docs; OpenTofu/Valkey/SeaweedFS/pgBackRest public repositories; Jira/GitHub/Make/Copilot pricing; n8n licensing guidance.

Vendor Claim != Runtime Proof.
No Evidence = No Progress.
