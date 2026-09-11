# 05_RUNTIME_READINESS_AND_BLOCKER_REGISTER

Session: SMEPLUS-26-09-11-DEVTOOL-VALIDATION-001
Status: CLI SMOKE PASS / AUTHENTICATED BENCHMARK PENDING

## Local Execution Environment
Available: node, npm, npx, git.
Initially not found: claude, codex, cursor, junie, gh.
Local npm registry access failed with EAI_AGAIN/getaddrinfo; this is classified as an environment/network blocker, NOT a candidate failure.

## Neutral Runtime Proof — GitHub Actions
Workflow: `.github/workflows/devtool-cli-smoke.yml`
Run ID: 34613164004
Commit: 36bac0ab5886dd39491c294ab82164996f6e5c30
Runner: Ubuntu 24.04 / ubuntu-24.04 image
GitHub token permission used by smoke run: contents: read; metadata: read.
No candidate API key was required for this smoke test.

### Results
| Candidate | Install | Version/Help | Verified Version | Runtime Disposition |
|---|---|---|---|---|
| Claude Code | PASS | PASS | 2.1.268 | CLI RUNTIME AVAILABLE |
| OpenAI Codex | PASS | PASS | codex-cli 0.154.0 | CLI RUNTIME AVAILABLE |
| Cursor Agent | PASS | PASS | 2026.09.10-fd3934a | CLI RUNTIME AVAILABLE |
| JetBrains Junie | PASS | PASS | 26.9.7 (3110.7) | CLI RUNTIME AVAILABLE |

All four matrix jobs completed successfully and uploaded separate evidence artifacts.

## Evidence Artifacts
- Claude artifact ID: 10268429901
- Codex artifact ID: 10269064299
- Cursor artifact ID: 10268949605
- Junie artifact ID: 10269555706

Each artifact contains version.txt, help.txt and run-metadata.txt.

## Credential Wiring Check
Repository indexed source search returned no references for:
- ANTHROPIC_API_KEY
- OPENAI_API_KEY
- CURSOR_API_KEY
- JUNIE_API_KEY

This does NOT prove repository secrets are absent; secret values/names are not inspected through source search. It only establishes that no current indexed source wiring was found.

## Governance Disposition
- CLI install/runtime availability proof: PASS for all four candidates.
- Authenticated AI task correctness/quality proof: NOT YET EXECUTED.
- Runtime PASS/FAIL scores for coding quality MUST NOT be inferred from this smoke result.
- No candidate may be declared final AI-coding winner until the frozen same-task benchmark is executed with controlled credentials, budget and permissions.

## Next Executable Gate
Run the frozen 15-scenario benchmark with authenticated candidate access in controlled branches/worktrees using the same base SHA, prompt hashes, acceptance criteria, network/secret boundaries and evidence schema.

## Boss Interaction Rule
No clarification requested. Continue all non-authenticated evidence, architecture, security, overlap, cost and benchmark-preparation work automatically. Surface any unresolved authenticated-runtime dependency only at the relevant Boss Final Gate.
