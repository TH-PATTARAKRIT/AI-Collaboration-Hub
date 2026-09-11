# 03_CAPABILITY_GAP_AND_ADMISSION_REGISTER

Session: SMEPLUS-26-09-11-DEVTOOL-VALIDATION-001
Status: ACTIVE / EVIDENCE-BASED ADMISSION

## Material Capability Gaps

| Gap | Existing Coverage | Disposition |
|---|---|---|
| Security scanning (SAST/dependency/secret/supply-chain) | Not yet proven complete in baseline | OPEN — prefer GitHub-native first |
| Performance/load testing | No canonical tool proven | OPEN |
| Observability/tracing | No canonical tool proven | OPEN |
| API contract testing | No canonical tool proven | OPEN |
| Database engineering/migration review | Partial via engineering process; no dedicated proof | OPEN |
| AI agent governance hardening | Tool-specific controls differ; comparative proof needed | OPEN |

## Candidate Admissions

### ADM-01 — JetBrains Junie
Status: ADMITTED AS MATERIAL CHALLENGER
Reason: Current official product positioning includes agentic coding workflows, CLI/headless operation and project-level instructions/skills. Must be benchmarked, not assumed superior.
Target capability: CAP-02 / CAP-03 / CAP-17.

### ADM-02 — GitHub Native Security Stack
Status: ADMITTED FOR EVIDENCE REVIEW
Scope: CodeQL/code scanning, dependency review, secret scanning and repository-native security controls where plan/repository support is available.
Reason: closes CAP-12 while minimizing tool sprawl and preserving GitHub evidence lineage.

### ADM-03 — Grafana k6
Status: ADMITTED AS PERFORMANCE/LOAD TEST CANDIDATE
Reason: tests-as-code model, CI integration, explicit pass/fail thresholds and API/load scenarios align with SMEsPlus NFR and SaaS capacity validation.
Target capability: CAP-13 / CAP-18.

### ADM-04 — OpenTelemetry
Status: ADMITTED AS OBSERVABILITY FOUNDATION CANDIDATE
Reason: vendor-neutral telemetry instrumentation is preferable to binding core application observability to a single backend. Backend/visualization remains separate decision.
Target capability: CAP-14.

## Admission Rules Applied
No tool is admitted for popularity alone. Admission indicates only that material evidence justifies further validation; it is not CORE approval.
