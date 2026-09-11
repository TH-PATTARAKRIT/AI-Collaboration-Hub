# [SMEPLUS-26-09-11-DEVTOOL-VALIDATION-001]
## Multi-State Controlled Validation Protocol

Status: VALIDATION STANDARD FOR FINALIST PROOF
Owner: SSA
SaaS/Cost Veto: PSPA
Final Approver: Boss
Clean Room: 100%

## Purpose
Convert documentation research into comparable SMEsPlus runtime evidence without testing irrelevant features.

## Universal Benchmark Contract
Every finalist test must freeze:
1. SMEsPlus-owned clean-room task/fixture.
2. Base commit/input hash.
3. Acceptance oracle and failure conditions.
4. Allowed network/secrets/tools.
5. Time budget and cost budget.
6. Output/evidence schema.
7. Independent reviewer.
8. No production access.

Score only capability used by SMEsPlus. `Unused Feature = 0 Selection Value`.

## STATE01 — Identity Proof
Mission tests:
- Resolve project/role/owner identity from canonical registries.
- Reject ambiguous owner/authority.
- Verify secrets are not exposed in identity artifacts.
- Runtime IAM pilot: service account, tenant/company context, MFA/admin policy and revocation.

Finalists: GitHub/Jira structured registry model; Keycloak for runtime IAM.

## STATE02 — Governance Proof
Mission tests:
- Missing owner -> HOLD.
- Missing reviewer -> HOLD.
- Unsupported PASS -> reject.
- Prohibited production action -> block.
- Policy change -> trace exact version/decision/evidence.

Finalists: GitHub Actions native validation; OPA supplement.
Success is deterministic rule enforcement, not number of policies supported.

## STATE03 — Architecture Proof
Use one clean-room SaaS cell scenario.
Test:
- create/update C4 views;
- change one relation and inspect diff;
- link ADR;
- validate API/event contracts in CI;
- AI reads model and identifies affected components.

Finalists: Structurizr + Mermaid; OpenAPI; AsyncAPI; bpmn.io where process architecture applies.

## STATE04 — Functional Proof
Use one clean-room ERP workflow requirement.
Test:
`evidence -> business rules -> process -> FDS -> acceptance criteria -> traceability`.
Measure:
- missing requirement detection;
- contradiction detection;
- traceability completeness;
- Thai terminology/localization preservation;
- human review effort;
- clean-room provenance.

Finalists: GitHub structured FDS + Jira + AI reviewer; BPMN supplement.

## STATE05 — UX/UI Proof
Use the same approved clean-room FDS.
Test:
- UX flow;
- role-specific screens;
- component reuse;
- design-token consistency;
- developer handoff;
- AI/code handoff;
- visual evidence;
- branch/source-of-truth behavior.

Finalists:
- Figma Design baseline.
- Figma Dev Mode/MCP.
- Lovable only as prototype/design-to-code challenger, not as assumed source of truth.
- Storybook after implementation begins.

Measure seat cost per actual role, not total feature count.

## STATE06 — Development Proof
Continue existing B01–B15 coding benchmark on frozen clean-room fixtures.
Mandatory tracks:
- Track N Neutral Harness.
- Track I Native Integration.

Separate:
- model score;
- agent/harness score;
- human intervention;
- accepted-task cost;
- evidence quality.

Finalists: Claude Code, Codex, Cursor, Junie, GitHub Copilot; others admitted only for material gap.

## STATE07 — Testing Proof
One vertical slice must exercise:
- unit/component;
- PostgreSQL-backed integration;
- API/event contract where applicable;
- browser E2E;
- visual/component state;
- performance thresholds;
- dynamic security scan;
- artifact/evidence retention.

Finalists: Playwright, Testcontainers, Pact where applicable, Storybook, k6, ZAP, GitHub Actions.
Measure flake rate and false positives, not test count.

## STATE08 — AI EOS / Automation Proof
One synthetic clean-room long-running job:
1. accept controlled prompt/job;
2. dispatch dummy/controlled executor;
3. checkpoint state;
4. simulate worker crash;
5. retry/recover;
6. pause for human Gate;
7. resume;
8. cap retries/cost;
9. preserve evidence;
10. fail deterministically on prohibited action.

Finalists:
- Hatchet — first pilot.
- Temporal — mandatory challenger.
- Trigger.dev — simpler challenger.
- BullMQ — queue-only control case.
- Make/n8n — integration-edge comparison only, not assumed AI EOS core.

Measure operational steps, recovery behavior, Postgres/resource footprint, developer complexity and cost.

## STATE09 — Infrastructure Proof
### OS
Same app/container/runtime tests on Debian 13 and Ubuntu 26.04 LTS:
- patch/update;
- Node/PostgreSQL compatibility;
- package availability;
- security baseline;
- restart/automation;
- provider image/support;
- team operations.

### Container
Podman/Quadlet:
- rootless service where applicable;
- restart after host reboot;
- health/rollback;
- log/evidence capture.

### Data services
- PostgreSQL backup/restore with pgBackRest.
- Valkey fail/restart behavior if cache introduced.
- NATS vs RabbitMQ using actual SMEsPlus event semantics.
- SeaweedFS vs managed object storage using attachment/evidence object workload.

Kubernetes/Ceph are admitted only if a scale/HA trigger is demonstrated.

## STATE10 — Production Operations Proof
Test in non-production environment:
- OpenTelemetry trace propagation;
- Prometheus SLI/alert;
- log tenant isolation/authentication;
- dashboard diagnosis;
- backup restore;
- deployment rollback;
- incident/change evidence.

Never use Prometheus as exact financial billing oracle.

## STATE11 — Knowledge Base Proof
Use a frozen evidence corpus:
- exact lookup;
- version/freshness detection;
- source citation;
- superseded-document handling;
- semantic retrieval benchmark if pgvector is enabled.

Baseline: GitHub canonical corpus. Docusaurus/pgvector must prove incremental value rather than duplicate truth.

## STATE12 — Current Context Proof
Generate context from canonical registers and deliberately inject:
- stale session;
- stale commit;
- contradictory Gate;
- missing owner;
- superseded evidence.

Pass only when generated Current Context identifies freshness/conflict and refuses unsupported progress.

## Final Evaluation Dimensions
Each applicable mission is evaluated on:
- Correctness / mission completion.
- Governance / authority boundary.
- Clean-room provenance.
- Security / tenant isolation.
- Reliability / recoverability.
- Automation / human intervention.
- Evidence / auditability.
- Integration complexity.
- Maintainability / exit portability.
- Time.
- Sustainable TCO.

Critical governance, tenant isolation, secret exposure, untraceable provenance or production-authority breach = zero-tolerance override.

## Gate
This protocol authorizes no production/development architecture freeze by itself. It defines how unresolved finalists must be proved before becoming canonical.
