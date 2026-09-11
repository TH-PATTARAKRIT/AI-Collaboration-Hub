# [SMEPLUS-26-09-11-DEVTOOL-VALIDATION-001]
## SMEsPlus 12-STATE Tool Operating Map — Technical Recommendation

Status: TECHNICAL RECOMMENDATION / AWAITING BOSS FINAL GATE
Owner: SSA
Co-Owner / SaaS Cost & Isolation Veto: PSPA
Clean Room: 100%

## Reading Rule
This map selects tools by mission. `Primary` means the preferred operating owner for that mission, not a universal winner for the State. `Supporting` closes a specific gap. `HOLD` means no freeze yet.

---

## STATE01 — Identity
**Primary:** GitHub structured Markdown/YAML/JSON registries.
**Supporting:** Jira for active responsibility; SOPS for encrypted configuration/secrets.
**Runtime IAM:** Keycloak = PILOT, not automatic core.

Operating contract:
`Identity definition -> versioned Git record -> active responsibility in Jira -> gate/evidence linkage`.

Do not use chat/Slack as canonical identity source.

---

## STATE02 — Governance
**Primary:** GitHub governance-as-code + Jira decision/work traceability.
**Enforcement:** GitHub Actions.
**Policy supplement:** OPA when deterministic policy evaluation is needed.
**Secret supplement:** SOPS; OpenBao only after dynamic-secret need is proven.

Mapped to proven State02 steps:
- Step01 Governance Baseline Inventory -> GitHub index/search + evidence register.
- Step02 Authority Conflict Resolution -> GitHub decision record + Jira escalation.
- Step03 Canonical RACI -> GitHub machine-readable RACI + Jira ownership mapping.
- Step04 Ownerless Execution Control -> CI/automation rule blocks ownerless package.
- Step05 Governance Index -> GitHub generated index.
- Step06 Gate Crosswalk -> machine-readable matrix + CI validation.
- Step07 Evidence & Approval Standard -> GitHub artifacts + Jira/Gate references.

Do not add a commercial GRC suite without a proven compliance gap.

---

## STATE03 — Architecture
**Primary canonical evidence:** GitHub docs-as-code + ADR.
**System model:** Structurizr DSL/C4 = PILOT.
**Lightweight diagrams:** Mermaid = KEEP.
**Process architecture:** bpmn.io = PILOT where BPMN is needed.
**API contract:** OpenAPI/Swagger.
**Event contract:** AsyncAPI.

Mapped to known STEP missions:
- STEP0301 Baseline -> GitHub/ADR/model index.
- STEP0302 Evidence Port/Gate B -> GitHub evidence packages + automated manifest/hash checks.
- STEP0303 Toolchain Matrix -> this current validation methodology should become the evidence refresh, not a feature-count table.
- STEP0304 -> Boss-confirmed deep-research parent; formal repository title not invented in this map.

Architecture truth remains textual/model-based and diffable; Figma is not architecture source of truth.

---

## STATE04 — Functional
**Primary:** SMEsPlus FDS in GitHub Markdown/YAML + traceability IDs.
**Work tracking:** Jira.
**Business process:** bpmn.io where formal BPMN adds clarity.
**Interface handoff:** OpenAPI/AsyncAPI when function crosses an API/event boundary.
**AI assistance:** pluggable ChatGPT/Claude/other research/review agents; no AI-generated FDS is approved by itself.

Known STEP:
- STEP0401 Evidence & Module Inventory Baseline -> GitHub manifests/registers and independent evidence review.

Recommended functional handoff contract:
`Evidence -> Business Rule -> Process -> FDS -> Acceptance Criteria -> Traceability -> Review -> Gate`.

Do not buy a heavyweight requirements suite until this low-cost structured approach fails measured usability/traceability criteria.

---

## STATE05 — UX/UI
**Primary:** Figma Design = RECOMMEND KEEP, subject to project workflow re-proof.
**Developer handoff:** Figma Dev Mode/MCP = PILOT selectively.
**Code/design mapping:** Code Connect = HOLD until Organization/Enterprise seat ROI is proven.
**Prototype accelerator:** Lovable = OPTIONAL SUPPLEMENT, not source of truth and not primary implementation path for existing SMEsPlus repository.
**Component operating system:** Storybook = PILOT after frontend stack pilot.
**Visual/runtime proof:** Playwright downstream in STATE07.

Operating contract:
`Approved FDS -> UX flow -> screen/design system -> Figma evidence -> design-to-code contract -> frontend implementation -> visual/runtime verification`.

Cost control: buy Full/Dev seats only for roles needing authoring/advanced handoff.

---

## STATE06 — Development
**Repository/PR:** GitHub.
**CI:** GitHub Actions, with self-hosted runners evaluated when minute/security economics justify.
**Backend runtime baseline:** Node.js 24 LTS + TypeScript.
**Database baseline:** PostgreSQL 18.x.
**Backend HTTP framework:** Fastify = FIRST PILOT; freeze only after representative ERP API benchmark.
**Frontend:** React + Vite = FIRST PILOT for authenticated ERP web application; SSR/full-stack framework added only if a real route/use case requires it.
**Component development:** Storybook = PILOT.

**AI Coding Executor:** HOLD FOR WINNER.
- Codex: B01 accepted with qualifications, but only repository-understanding scenario.
- Claude Code: auth exists but credit/billing blocked B01.
- Cursor: auth absent.
- Junie: CLI/headless installed and proven, auth absent.
- GitHub Copilot: admitted material GitHub-native challenger.

AI EOS requirement: the coding executor must remain replaceable through a common job/evidence contract.

Do not let agent preference determine framework/database architecture.

---

## STATE07 — Testing
**Unit/component:** Node/TypeScript test runner decision remains PILOT; Storybook + Vitest integration is a strong frontend route and requires benchmark on project fixture.
**Integration:** Testcontainers = RECOMMEND SUPPLEMENT.
**API/event contract:** Pact = use only where consumer-driven contract testing is applicable.
**Browser E2E/runtime evidence:** Playwright = RECOMMEND PRIMARY.
**UI component states:** Storybook = RECOMMEND SUPPLEMENT.
**Performance/load:** Grafana k6 = RECOMMEND PRIMARY for automated thresholds.
**Dynamic security:** OWASP ZAP = RECOMMEND SUPPLEMENT.
**CI/evidence:** GitHub Actions + artifacts/attestations.

Evidence contract:
`test ID -> frozen input -> environment -> tool/version -> result -> trace/log/screenshot -> defect -> re-test -> verifier -> gate impact`.

No screenshot alone proves business correctness; no test log alone proves visual correctness.

---

## STATE08 — AI Execution / AI EOS
**AI EOS:** SMEsPlus-owned control plane and operating semantics.
**Durable orchestration:** Hatchet = FIRST PILOT; Temporal = mandatory challenger.
**Simple/background job challenger:** Trigger.dev.
**Queue specialist:** BullMQ only when queue semantics are sufficient.
**Integration edge:** direct API/webhook/native connector first; Make and n8n only when they close a measured connector gap.

Make status: `NOT IN OPERATIONAL USE / LEARNING REFERENCE ONLY`.
n8n status: `CHALLENGER WITH LICENSING CONSTRAINTS FOR EMBEDDING/CLIENT WORKFLOWS`.

Pilot acceptance must prove:
`job state + idempotency + timeout + retry + resume/replay + human gate + cost ceiling + evidence + agent adapter + failure recovery`.

Do not build AI EOS around one agent/vendor.

---

## STATE09 — Infrastructure
**OS finalists:** Ubuntu 26.04 LTS vs Debian 13.6 — FINAL CHOICE HOLD pending provider/team/patch/runtime benchmark.
**Container runtime:** Podman + Quadlet/systemd = FIRST PILOT.
**Kubernetes:** HOLD until objective scale/HA/placement trigger exists.
**Reverse proxy/TLS:** Caddy = FIRST PILOT; NGINX = fallback/challenger.
**Database:** PostgreSQL 18.x = RECOMMEND CORE.
**Cache:** Valkey = PILOT.
**Messaging:** NATS vs RabbitMQ quorum queues = benchmark by event/delivery mission.
**IaC:** OpenTofu.
**Host configuration/deploy:** Ansible.
**Object storage:** SeaweedFS vs managed S3-compatible service = pilot/TCO comparison; Ceph HOLD until scale/combined storage need.
**PostgreSQL backup:** pgBackRest = RECOMMEND PRIMARY candidate, restore drill mandatory.

Simple-road default:
`Linux -> Podman/Quadlet -> Caddy -> Node cells -> PostgreSQL -> optional Valkey/message/object services`.

---

## STATE10 — Production Operations
**Instrumentation:** OpenTelemetry.
**Metrics/alerts:** Prometheus + Alertmanager.
**Logs:** Loki = PILOT only behind authenticated tenant-aware proxy/control.
**Dashboards:** Grafana OSS.
**Backup/restore:** pgBackRest + object/offsite retention layer.
**Deploy/config:** GitHub Actions + OpenTofu + Ansible + Podman, gated.
**Incident/change:** Jira + GitHub evidence/change records.

Hard rule: Prometheus is operations telemetry, not canonical financial usage metering. Exact SaaS metering must be application-owned and auditable.

Production deployment remains Boss-gated.

---

## STATE11 — Knowledge Base
**Canonical source:** GitHub reviewed Markdown/YAML/JSON + versioned evidence links.
**Human-friendly portal:** Docusaurus = OPTIONAL generated view.
**Semantic retrieval:** PostgreSQL + pgvector = PILOT only when benchmark proves need.
**AI summaries/indexes:** derived, versioned, source-linked; never overwrite canonical evidence.

Do not create a second paid knowledge source of truth while GitHub already satisfies canonical versioning and review.

---

## STATE12 — Current Context
**Canonical machine context:** generated `CURRENT_CONTEXT.md/json/yaml` in GitHub from controlled registers.
**Live work/status:** Jira.
**Future execution state:** AI EOS state store after STATE08 proof.
**Notifications only:** Slack/chat/email; never canonical status.

Minimum current-context payload:
`project -> STATE -> STEP -> session -> prompt -> gate -> owner -> reviewer -> evidence pointers -> blockers -> carry-forward -> next authorized action -> freshness timestamp`.

---

# Cross-State Operating Backbone
Recommended common backbone:

`GitHub = canonical artifacts/evidence/source`
`Jira = active work/owner/traceability`
`Figma = UX design authority`
`GitHub Actions = CI/control automation`
`Playwright = browser runtime evidence`
`OpenAPI/AsyncAPI/BPMN/C4 = machine-readable design contracts by mission`
`Linux + Node.js LTS + PostgreSQL = low-license-cost runtime foundation`
`OpenTelemetry/Prometheus = operations visibility`
`AI EOS = future owned orchestration/control plane`
`AI coding/review models = pluggable executors, not architecture owners`

# Tools Explicitly Not Frozen
1. AI coding winner — comparative authenticated runtime incomplete.
2. Ubuntu vs Debian default OS — both viable; empirical/provider choice pending.
3. Hatchet vs Temporal AI EOS engine — pilot required.
4. NATS vs RabbitMQ — messaging mission benchmark required.
5. Self-host SeaweedFS vs managed object storage — TCO/DR benchmark required.
6. Keycloak — runtime IAM pilot required.
7. Fastify + React/Vite — representative clean-room ERP vertical-slice proof required before architecture freeze.
8. Loki — tenant isolation/authentication proof required.

# AI EOS Learning Output
For each future execution mission, AI EOS must learn/store:
- State and STEP/mission ID.
- Primary tool and allowed alternatives.
- Required input contract.
- Allowed/prohibited actions.
- Expected output/evidence contract.
- Version/license/provenance constraints.
- Time/cost ceiling.
- Retry/failure policy.
- Human reviewer/gate.
- Fallback/exit strategy.

This map is a technical recommendation, not Boss approval.
