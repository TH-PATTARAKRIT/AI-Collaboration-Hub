# L1-L12 Very Deep Research Standard

Apply each level when relevant to the canonical target. Record explicit N/A rationale where a level is genuinely not applicable.

- L1 Domain Understanding — purpose, actors, business objective, boundaries.
- L2 UI / Field / Configuration — screens, fields, states, configuration switches, role exposure.
- L3 Function — behavior, rules, validations, transitions, outputs.
- L4 Cross-Module — upstream/downstream dependencies, handoffs, ownership, shared identities.
- L5 Whole-System — effect on end-to-end system behavior, reporting, audit, operations.
- L6 Contradiction / Edge Case — negative paths, cancellation, reversal, partial states, concurrency, unusual values.
- L7 Control / Internal Control — approvals, segregation, auditability, fraud/error prevention, authorization.
- L8 Data / Identity / Immutability — canonical identity, lifecycle, retention, mutation rules, event/evidence integrity.
- L9 SaaS / Multi-Tenant / Multi-Company — tenant isolation, company boundary, context switching, shared master rules.
- L10 Migration / Historical — legacy mapping, opening states, historical semantics, archival and replay behavior.
- L11 Reconciliation / End-to-End Proof — financial/operational reconciliation, source-to-result traceability, proof of completeness.
- L12 Adversarial Challenge — actively attempt to falsify the conclusion and expose control or proof weakness.

## Completion rule

A target is not Research-Complete solely because L1-L3 are understood. Determine applicability across L1-L12 and record gaps explicitly.

For Accounting, security boundaries, critical controls, inventory valuation, posting, identity, and reconciliation, use the strongest reasonable interpretation of the levels.
