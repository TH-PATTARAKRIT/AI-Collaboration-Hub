# Proof and Evidence Standard

## Mandatory five proof layers

Preserve the project's canonical layer names if supplied. Otherwise use these categories:

1. Definition / Source / Structural Proof
2. Runtime Reachability Proof
3. Configuration / Role / Condition Proof
4. Scenario / Transaction / Cross-Module Proof
5. Reconciliation / Independent / Adversarial / End-to-End Proof

A missing applicable layer is `NOT PROVEN`, not PASS.

## Evidence traceability fields

Use as many as available and required:

- Evidence ID
- Evidence Type
- Source / System
- Repository
- File Path
- Document / Section / Line or Range
- Commit SHA / Last Verified SHA
- URL
- Screenshot ID
- Runtime Scenario
- Configuration State
- Database Evidence
- Test Case
- Date
- Reviewer
- Verification Status
- Superseded Status

## Evidence states

- APPROVED
- REVIEWED
- DRAFT
- SUPERSEDED
- NO SOURCE
- INVALID
- UNKNOWN

## Evidence quality rules

- Never fabricate a file, line, screenshot, URL, commit, test result, runtime state, or database result.
- State `SOURCE UNAVAILABLE` when an authorized source cannot be accessed.
- State `EVIDENCE POINTER NOT VERIFIED` when a pointer exists but cannot be verified.
- Keep contradictory evidence visible until formally resolved.
- Preserve superseded evidence for lineage; do not use it as current proof.
- Separate observed facts from conclusions, inferences, assumptions, unknowns, contradictions, and gaps.

## Function proof dimensions

Track when applicable:

- Source Presence
- Runtime Reachability
- Configuration Reachability
- Optional Function Reachability
- Role / Access Reachability
- Cross-Module Handoff
- Data Integrity
- Control Integrity
- SaaS Isolation
- Migration / Historical
- Reconciliation
- Evidence Integrity
