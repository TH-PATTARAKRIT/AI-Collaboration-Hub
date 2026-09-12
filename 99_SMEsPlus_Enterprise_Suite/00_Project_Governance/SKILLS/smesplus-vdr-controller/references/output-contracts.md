# Output Contracts

## Function evidence record

Use this structure when reviewing a canonical function:

```text
Function-ID:
Function Name:
Domain:
Module:
Owner:

Research Depth:
L1: PASS/GAP/N-A
L2: PASS/GAP/N-A
L3: PASS/GAP/N-A
L4: PASS/GAP/N-A
L5: PASS/GAP/N-A
L6: PASS/GAP/N-A
L7: PASS/GAP/N-A
L8: PASS/GAP/N-A
L9: PASS/GAP/N-A
L10: PASS/GAP/N-A
L11: PASS/GAP/N-A
L12: PASS/GAP/N-A

Proof Requirements:
Proof Layer 1:
Proof Layer 2:
Proof Layer 3:
Proof Layer 4:
Proof Layer 5:

Source Presence: PASS/FAIL/N-A/UNKNOWN
Runtime Reachability: PASS/FAIL/N-A/UNKNOWN
Configuration Reachability: PASS/FAIL/N-A/UNKNOWN
Optional Reachability: PASS/FAIL/N-A/UNKNOWN
Cross-Module Handoff: PASS/FAIL/N-A/UNKNOWN
Evidence Integrity: PASS/HOLD/FAIL
Contradictions:
Open Gaps:
Unknowns:
Zero-Tolerance Finding: NONE/OPEN/FAIL
Material Delta: YES/NO/UNKNOWN
Coverage Eligibility: ELIGIBLE/NOT ELIGIBLE
Disposition: PASS RECOMMENDATION/CONDITIONAL PASS RECOMMENDATION/HOLD RECOMMENDATION/FAIL RECOMMENDATION
Boss Decision: PENDING/APPROVED/REJECTED/RETURNED
```

## Coverage review

Report:

- Denominator state and version/reference
- Formal vs diagnostic status
- Applicable dimensions and exact percentages
- dimensions below 96%
- Zero-Tolerance result
- unresolved critical gaps
- denominator/control issues
- resulting AI recommendation
- Boss Decision status

Never report a Formal Coverage percentage if denominator state is not FROZEN.

## Boss Gate package

Default sections:

1. Session / Scope
2. Current Gate
3. Canonical Denominator Status
4. Research and Proof Summary
5. Applicable Coverage Dimensions
6. Zero-Tolerance / Critical Controls
7. Open Gaps / Contradictions / Unknowns
8. Material Delta and Carried-Forward Evidence
9. Independent QA Findings
10. Adversarial Challenge Findings
11. Evidence Integrity / Missing Evidence
12. AI Gate Recommendation
13. Boss Decision: PENDING unless explicitly supplied

## Gap register fields

Gap ID | Function ID | Dimension | Severity | Evidence | Owner | Required Action | Gate Impact | Status.
