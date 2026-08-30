# BOSS DECISION — EXPERT IDTM & TEST TOLERANCE GOVERNANCE

Decision ID: SMEPLUS-BDR-IDTM-2026-08-30-001
Project: SMEsPlus Enterprise Suite
Date: 2026-08-30
Authority: Boss
Status: APPROVED / EFFECTIVE

## Decision

Boss approves the formal appointment and addition of:

**EXPERT IDTM — Independent Deep Test Matrix & System Verification Team**

as an independent project verification unit using 100% AI execution against the approved 10-Dimension Deep Test Matrix.

Boss also approves Test Case Tolerance Governance as a mandatory project control.

## Tolerance Ruling

Every controlled Test Case must define its Tolerance target before execution.

```text
0% <= Test Case Failure/Deviation Tolerance <= 0.001%
```

No ordinary Test Case may declare a tolerance above `0.001%` without a subsequent explicit Boss ruling.

A stricter target is always permitted.

## Zero-Tolerance Ruling

The following categories are `Tolerance = 0` unless Boss issues a specific written exception:

- Tenant data leakage / cross-tenant access
- Unauthorized privilege escalation
- Debit/Credit imbalance in a posted accounting entry
- Silent financial data corruption
- Unauthorized financial posting
- Duplicate financial posting caused by system failure or replay
- Irrecoverable controlled-data loss
- Critical inventory conservation/integrity violation
- Audit evidence tampering or unauthorized audit-trail suppression
- Statutory/compliance invariant explicitly defined as exact
- Security isolation breach classified Critical

A single confirmed occurrence in a zero-tolerance category is a Gate-blocking failure until remediated and independently retested, unless Boss explicitly accepts the risk.

## Measurement Rule

Tolerance is meaningful only when its metric, unit and denominator are declared and frozen before execution.

For occurrence-based error/failure rates:

```text
0.001% = 0.00001
Allowed integer failures = floor(denominator x 0.00001)
```

Therefore, for fewer than 100,000 controlled observations, an occurrence-based tolerance ceiling of 0.001% permits zero whole failures.

Performance/SLO thresholds, response-time targets and legal rounding rules are separate acceptance criteria and must not be misrepresented as permission for data-integrity or functional defects.

## Zero-Bug Ruling

`0 BUG FOUND` is not automatic evidence of zero defects.

When IDTM reports zero defects after full matrix execution, the project must execute the Zero-Defect Challenge Protocol to verify that the test system itself is capable of detecting faults.

This includes controlled Mutation Testing / Seeded Defects, adversarial input, property-based tests, state-space traversal, concurrency amplification, chaos/fault injection and independent review as applicable.

Critical injected faults must have a miss tolerance of `0`.

For non-critical controlled injected-fault detection, the miss-rate target must not exceed `0.001%`; where the sample size is insufficient to permit a whole miss under that ceiling, zero misses are allowed.

## Mandatory Placement

```text
Team C — Development
→ Team D — Independent QA / Clean-room / Compliance
→ IESA Pre-Assurance Challenge (no final verdict)
→ EXPERT IDTM — 100% AI 10-Dimension Deep Test Matrix
→ Independent Deep Test Matrix Gate
→ EXPERT IESA — Final ERP & SaaS Assurance
→ Pre-Production Enterprise & SaaS Assurance Gate
→ Boss Release / Production Decision
→ Production / Customer Use
```

## Defect Remediation Loop

```text
IDTM Defect / Gap
→ Team C Remediation
→ Team D Regression / Compliance Recheck
→ IDTM Independent Retest
→ IESA Final Assurance only when the controlled evidence is complete
```

## Lifecycle Ruling

A new numbered STATE is not required at this time.

IDTM is established as a mandatory independent verification layer within the controlled Testing/UAT lifecycle and before IESA Final Assurance.

If evidence later shows that IDTM requires a standalone lifecycle STATE, PMO may submit a controlled STATE-baseline Change Request for Boss approval. No STATE renumbering is authorized by this decision.

## Final Authority

IDTM produces independent deep-test evidence and Gate recommendations. IESA independently assesses the system-level evidence. Neither replaces Boss approval.

**Boss remains the Sole Final Approver.**

## Governing Principles

**No Evidence = No Progress**

**Never Skip Gate**

**Zero bugs found is not evidence of zero bugs**

**Boss = Sole Final Approver**
