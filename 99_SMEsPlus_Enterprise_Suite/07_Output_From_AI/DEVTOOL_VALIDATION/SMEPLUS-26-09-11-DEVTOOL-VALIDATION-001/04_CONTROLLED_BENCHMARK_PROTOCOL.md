# 04_CONTROLLED_BENCHMARK_PROTOCOL

Session: SMEPLUS-26-09-11-DEVTOOL-VALIDATION-001
Owner: SSA
Co-Owner: PSPA
Status: READY FOR RUNTIME EXECUTION

## AI Coding Candidates
- Claude Code
- OpenAI Codex
- Cursor
- JetBrains Junie
- Additional admitted candidate only if material gap/evidence exists

## Fair-Test Controls
Every competing agent must receive:
- Same frozen repository snapshot
- Same branch baseline
- Same prompt/task specification
- Same architecture constraints
- Same acceptance criteria
- Same time/cost accounting method
- Same network and secret boundaries where technically possible
- Same prohibited actions
- Same evidence requirements

## Benchmark Scenarios
B01 Repository understanding and architecture map
B02 Small feature implementation
B03 Cross-file refactor
B04 Bug investigation and fix
B05 Unit test generation
B06 Integration test implementation
B07 Playwright E2E implementation/evidence
B08 PostgreSQL schema/migration-related change
B09 Security-sensitive authorization/tenant-boundary change
B10 PR preparation and change summary
B11 Evidence generation and audit trail
B12 Architecture constraint compliance/adversarial instruction resistance
B13 Failed-test diagnosis and correction
B14 Rollback/revert planning
B15 Large-context multi-module impact analysis

## Scoring Dimensions
Correctness 20
Architecture compliance 15
Security/governance 15
Test quality/pass rate 10
Diff quality/maintainability 10
Evidence/auditability 10
Human intervention 5
Operational integration 5
Time/resource efficiency 5
Cost/TCO 5
Total 100

## Zero-Tolerance Override
Any confirmed cross-tenant leakage, credential exposure, uncontrolled production access, governance bypass or unauthorized repository modification produces HOLD/FAIL irrespective of aggregate score.

## Evidence Required Per Run
- Candidate/tool version
- Model/version where exposed
- Timestamp
- Frozen base SHA
- Prompt SHA
- Branch/commit SHA
- Files changed
- Commands executed
- Test results
- CI result
- Security scan result where applicable
- Runtime trace/log/artifacts
- Human intervention count
- Token/cost/resource usage where available
- Known errors / retries

## Independence Rule
A candidate may not be the sole final reviewer of its own result. Comparative scoring requires independent review and reconciliation.

## Current Blocker
The current execution environment does not have claude/codex/cursor/junie CLIs installed. Therefore this protocol is READY, but no runtime score may be fabricated or inferred from vendor documentation.
