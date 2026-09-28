# Canonical Denominator and Coverage Control

## Denominator states

Use:

- PROPOSED
- PENDING
- FROZEN
- REOPENED
- SUPERSEDED

Only `FROZEN` permits Formal Coverage calculation.

## Canonical universes

Maintain as applicable:

- Question Universe
- Function Universe
- VDR Target Universe
- Zero-Tolerance Universe
- Coverage Dimension Universe
- Cross-Module Handoff Universe
- Contradiction Register
- Open Gap Register
- Unknown Register

Use stable Function IDs for canonical functions.

## Atomic reconciliation

Before freeze, detect:

- duplicate or semantic duplicate functions,
- incorrect split/merge,
- missing functions,
- orphan questions/evidence,
- denominator contamination,
- invalid exclusions,
- uncontrolled N/A,
- cross-module ownership collisions,
- incorrect optional/mandatory classification.

Do not calculate Formal Coverage during reconciliation.

## Coverage dimensions

Support at least:

- Research Coverage
- Source Presence Coverage
- Runtime Reachability Coverage
- Configuration Reachability Coverage
- Optional Function Reachability
- Evidence Coverage
- Cross-Module Coverage
- Control Coverage
- Data Integrity Coverage
- SaaS / Multi-Company Coverage
- Migration / Historical Coverage
- Reconciliation Coverage
- Adversarial Challenge Coverage

Project governance may add dimensions. Do not silently remove an applicable dimension.

## Thresholds

- Every applicable dimension: >= 96%.
- Critical / Zero-Tolerance: 100%.
- Any unresolved critical gap can force HOLD regardless of percentages.
- Overall averages are diagnostic only; they cannot override per-dimension thresholds.

Example: 99, 100, 97, 94, 98 averages above 96, but 94 is below the floor, therefore HOLD.

## Post-freeze changes

A frozen denominator can change only through controlled re-open/change-control with rationale, impact analysis, lineage, and Boss approval. Never silently mutate it after results are known.
