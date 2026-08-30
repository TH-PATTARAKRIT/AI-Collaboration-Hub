# TEST CASE TOLERANCE & ZERO-DEFECT CHALLENGE POLICY

Policy ID: SMEPLUS-POL-TEST-TOL-001
Version: v1.0
Status: BOSS APPROVED / MANDATORY
Effective Date: 2026-08-30
Project: SMEsPlus Enterprise Suite
Applies To: Team C testing support, Team D, EXPERT IDTM, EXPERT IESA and all AI test executors/reviewers

## 1. Objective

Define measurable tolerance targets for every controlled Test Case and prevent `0 BUG FOUND` from being treated as sufficient evidence of system correctness without proving test adequacy.

## 2. Global Tolerance Ceiling

Every Test Case must declare a Tolerance before execution.

```text
0% <= T_case <= 0.001%
```

Where `T_case` is the permitted failure/deviation rate for the specific controlled metric.

A Test Case may set `T_case = 0%` or any stricter value below the project ceiling. A value above `0.001%` is prohibited unless Boss issues a written exception.

## 3. Mandatory Tolerance Fields

Each Test Case record must include:

- Tolerance ID
- Test ID / Matrix Version
- Risk Criticality
- Measured Metric
- Unit
- Denominator / observation count or controlled basis
- Target value / expected invariant
- Tolerance percentage
- Absolute threshold where required for a non-error operational metric
- Rationale
- Evidence method
- Gate impact if exceeded

A percentage without a defined denominator is `INVALID TOLERANCE / EVIDENCE MISSING`.

## 4. Zero-Tolerance Classes

`Tolerance = 0` is mandatory for Critical integrity/security classes including:

1. Tenant data leakage or cross-tenant unauthorized access
2. Critical privilege escalation
3. Posted accounting Debit/Credit imbalance
4. Silent financial data corruption
5. Unauthorized financial posting
6. Duplicate financial posting caused by replay/system failure
7. Irrecoverable controlled-data loss
8. Critical inventory conservation/integrity breach
9. Unauthorized audit-trail suppression/tampering
10. Exact statutory/compliance invariants defined by approved requirements
11. Critical security isolation breach

Any confirmed occurrence causes a Gate HOLD until remediation and independent retest, unless Boss explicitly accepts the risk in writing.

## 5. Count-Based Interpretation

For occurrence-based failures:

```text
0.001% = 0.00001
Allowed failures = floor(N x 0.00001)
```

Examples:

- N = 10,000 -> allowed whole failures = 0
- N = 99,999 -> allowed whole failures = 0
- N = 100,000 -> maximum allowed whole failures = 1 for a non-zero-tolerance class
- N = 1,000,000 -> maximum allowed whole failures = 10 for a non-zero-tolerance class

This mathematical ceiling does not automatically make an observed failure acceptable. Severity, business impact, systemic nature and IESA assessment still apply.

## 6. Functional Error Tolerance vs Operational Threshold

Do not confuse functional/data-integrity error tolerance with operational thresholds.

Examples:

- Accounting rounding must follow the approved rounding rule exactly; the project must not hide incorrect rounding behind a generic percentage tolerance.
- API latency may have an approved SLO threshold in milliseconds; that SLO is not permission for functional failure.
- Recovery Time Objective and Recovery Point Objective are controlled operational thresholds, not data-corruption tolerance.

## 7. Zero-Defect Challenge Protocol (ZDCP)

Trigger condition:

```text
Approved Matrix Execution = 100%
AND
Confirmed Bugs Found = 0
```

Required response:

```text
ZERO DEFECT DETECTED
→ TEST ADEQUACY CHALLENGE REQUIRED
→ NO PRODUCTION-READINESS CONCLUSION YET
```

Mandatory challenge methods, as applicable:

- Mutation Testing
- Blind Seeded Defect Testing
- Property-Based Testing
- Fuzzing / Adversarial Input
- Boundary-Value Amplification
- State-Space / Lifecycle Traversal
- Cross-Domain Reconciliation
- Concurrency Amplification / repeated timing variation
- Chaos / Fault Injection
- Independent AI Test Generation
- Independent Oracle / Evidence Review
- IESA Pre-/Post-Challenge of Test Adequacy

## 8. Fault-Detection Adequacy Target

Critical controlled injected faults:

```text
Miss Tolerance = 0%
```

Non-critical controlled injected faults:

```text
Miss Rate Target <= 0.001%
```

The injected-fault denominator must be frozen before execution. If the denominator is too small to permit one whole miss under the 0.001% ceiling, zero misses are allowed.

A seeded/mutation defect that escapes detection is not merely a product defect result; it is a `TEST ADEQUACY GAP` and requires improvement of the matrix/oracle before zero-defect evidence can be trusted.

## 9. Required Gate Logic

```text
Tolerance exceeded
→ FAIL / HOLD

Critical zero-tolerance occurrence
→ CRITICAL HOLD

0 bugs found without ZDCP
→ TEST ADEQUACY NOT PROVEN / HOLD

ZDCP detects escaped seeded faults beyond tolerance
→ MATRIX INADEQUATE / REDESIGN / RETEST

Matrix + ZDCP within approved tolerance
→ READY FOR IESA FINAL ASSURANCE
```

## 10. Prohibited Practices

- Changing a Tolerance after seeing Actual Results to create a PASS
- Changing the denominator after execution without controlled re-baselining
- Averaging a Critical defect into a low overall failure rate
- Declaring 100% bug-free from 100% Test Matrix execution
- Using performance tolerance to excuse financial/data-integrity errors
- Hiding `BLOCKED`, `UNKNOWN` or `EVIDENCE MISSING` inside PASS statistics
- Allowing the code-authoring AI to be the sole judge of its own test adequacy

## 11. Governing Formula

```text
Approved Coverage
+ Controlled Tolerance
+ Independent Evidence
+ Adversarial Proof
+ Test Adequacy Proof
+ Independent Assurance
= Evidence suitable for Boss decision
```

## 12. Authority

This policy does not authorize Development, Release or Production.

**Boss is the Sole Final Approver.**

**No Evidence = No Progress.**

**Never Skip Gate.**
