# 02_CURRENT_TOOL_BASELINE_AND_CANDIDATE_UNIVERSE

Session: SMEPLUS-26-09-11-DEVTOOL-VALIDATION-001
Status: ACTIVE — NOT FINAL FREEZE

## Historical / Current Baseline
Historical SMEsPlus evidence identifies ChatGPT as architecture/review/governance, Claude Code as engineering, GitHub as control, Jira as execution, Figma as design authority and Make as integration. This baseline is historical evidence only and does not confer automatic PASS.

## Candidate Universe — Round 1

| Capability | Candidate(s) | Current Disposition |
|---|---|---|
| Architecture / Research / Review | ChatGPT | INCUMBENT / RE-PROVE WHERE MATERIAL |
| AI Coding Agent | Claude Code | INCUMBENT PRIMARY BASELINE / NOT FROZEN |
| AI Coding Agent | OpenAI Codex | MAJOR CHALLENGER |
| AI Coding Agent / Agent Host | Cursor | CHALLENGER |
| AI Coding Agent / Agent Host | JetBrains Junie | NEW MATERIAL CHALLENGER — ADMITTED FOR EVIDENCE REVIEW |
| Source Control | GitHub | STRONG CORE CANDIDATE |
| CI/CD | GitHub Actions | STRONG CORE CANDIDATE |
| PMO / Traceability | Jira | STRONG CORE CANDIDATE |
| UI/UX / Design-to-Code | Figma | STRONG CORE CANDIDATE |
| E2E / Runtime Evidence | Playwright | STRONG CORE CANDIDATE |
| Integration Automation | Make | INCUMBENT BASELINE / NOT FROZEN |
| Integration Automation | n8n | CHALLENGER |
| IDE / Agent Host | VS Code | REMOVED / NOT IN USE / EXCLUDED |

## Capability-Gap Admission Queue
The following categories are OPEN for candidate search because the current baseline does not yet prove complete coverage:
- SAST / Dependency / Secret / Supply-chain security
- Performance / Load testing
- Observability / distributed tracing
- API contract / integration testing
- Database engineering / migration review
- AI agent policy / sandbox / audit hardening

Candidate admission rule: add a tool only when it closes a material capability gap or materially improves security, governance, cost, reliability or maintainability.

## Runtime Availability Check — Current Execution Environment
Verified in current runtime:
- node: AVAILABLE
- npm/npx: AVAILABLE
- git: AVAILABLE
- claude CLI: NOT FOUND
- codex CLI: NOT FOUND
- cursor CLI: NOT FOUND
- junie CLI: NOT FOUND
- gh CLI: NOT FOUND

Therefore no AI coding candidate may be marked runtime-PASS from this environment yet. Documentation evidence and runtime evidence remain separate.

## Selection Rule
No Predetermined Winner. Existing tool != automatic PASS. Boss preference != technical score. Vendor claim != runtime proof.
