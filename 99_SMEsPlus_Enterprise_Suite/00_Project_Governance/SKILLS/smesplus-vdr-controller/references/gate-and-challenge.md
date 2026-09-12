# Gate, Independent QA, and Adversarial Challenge

## Pre-freeze independent review

Ask:

- What is missing or duplicated?
- What is incorrectly merged, split, excluded, or marked optional?
- Are Zero-Tolerance controls complete?
- Does another module own this function?
- Is the target a function, configuration, control, handoff, or evidence target?
- Could denominator design bias the score?

Output `PRE-FREEZE REVIEW: PASS` or `PRE-FREEZE REVIEW: HOLD` with reasons.

## Independent QA

Challenge both conclusion and proof. Look for:

- confirmation bias,
- missing negative scenarios,
- invalid inference,
- wrong ownership,
- source/runtime mismatch,
- hidden configuration dependencies,
- role/access bypass,
- cross-company or cross-tenant leakage,
- reconciliation weakness,
- unsupported N/A,
- stale or superseded evidence,
- denominator distortion.

## Adversarial questions

Attempt to disprove important findings:

- What would make this conclusion false?
- Can the function exist in source but be unreachable?
- Can it run only under hidden configuration?
- Can another role bypass the expected control?
- Can another company or tenant see this record?
- Does cancellation, reversal, return, or partial completion break the flow?
- Does historical/migrated data behave differently?
- Can a cross-module handoff lose identity or semantics?
- Is evidence stale?
- Does the test prove the function or only the UI?

## Gate chain

Evidence -> Research Review -> Proof Verification -> Independent QA -> Adversarial Challenge -> Coverage Review -> Gate Recommendation -> Boss Decision.

AI may recommend PASS, CONDITIONAL PASS, HOLD, or FAIL. Boss is the sole Final Approver.
