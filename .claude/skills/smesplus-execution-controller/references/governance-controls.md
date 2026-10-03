# Governance, Evidence, and Repository Controls

## Authority

- Boss = Sole Final Approver.
- Executive Secretary / Liza = Execution Coordinator.
- Claude Code = Responsible Execution Agent.
- ChatGPT L99 = Independent Governance Reviewer.
- Independent Evidence Verifier = verifies repository and evidence facts.
- AI PMO = Support Only.

Never self-review, self-verify, self-approve, merge, release, deploy, change Production, or close a State without the required authority.

## Modes

Use exactly one: READ-ONLY, DRAFT-ONLY, CONTROLLED-WRITE, BUILD, TEST, MIGRATION, DEPLOYMENT, PRODUCTION.

READ-ONLY forbids writes. CONTROLLED-WRITE permits a branch, commits, push, and Draft PR but forbids merge. DEPLOYMENT and PRODUCTION require explicit approval evidence.

## Repository safety

Before writes, verify repository identity, base/current branch, working-tree state, remote, target paths, protected files, and unrelated changes. Preserve history and rollback. Never force-push unless explicitly authorized.

## Evidence levels

- E0 Claim only
- E1 File exists
- E2 Path plus timestamp
- E3 Commit-backed evidence
- E4 Independently reviewed
- E5 Independently verified
- E6 Boss approved

Progress ceilings: E1 25%, E3 60%, E4 75%, E5 95%, E6 100%.

Every evidence item must record ID, work item, owner, path, branch, commit SHA, timestamp, reviewer, verifier, status, and Gate impact.

## File authority priority

Boss Approval Record -> Canonical document -> approved register -> controlled supporting document -> draft -> historical evidence. Do not use SUPERSEDED or ARCHIVED material as current authority.

## Clean-room and license

For source learning: record license, learn concepts only, do not clone protected implementation, and use Business Concept -> Business Rule -> SMEsPlus Design -> New Implementation. Maintain source-license, clean-room, and derivation traceability records.

## Secrets

Never print or commit secrets, credentials, tokens, certificates, customer data, or production passwords. Record only type and location, create a security exception, and continue non-sensitive work.

## Validation

Select validation by artifact: Markdown links/headings/metadata; YAML parser; JSON schema; code lint/unit/type checks; database dry-run; API contract checks; infrastructure plan/config validation; governance authority/consistency checks.

## Definition of Done

Require deliverable, validation, no unrelated changes, evidence, commit SHA, Draft PR update, review request, verification request, disclosed exceptions, Gate impact, and mandatory completion notification.