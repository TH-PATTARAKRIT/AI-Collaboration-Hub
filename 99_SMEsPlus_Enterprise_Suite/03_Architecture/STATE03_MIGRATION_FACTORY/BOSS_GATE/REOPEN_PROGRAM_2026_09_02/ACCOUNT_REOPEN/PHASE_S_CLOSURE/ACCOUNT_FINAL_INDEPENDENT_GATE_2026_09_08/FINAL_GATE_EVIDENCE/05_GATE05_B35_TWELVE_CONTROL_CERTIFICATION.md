# GATE 05 — B-35 FULL TWELVE-CONTROL CERTIFICATION

Verifier: GPT-5.6 Sol independent verifier
Timestamp: 2026-09-08T20:19:00+0700
Control branch: `audit/gpt56sol-account-phase-s-final-independent-gate-2026-09-08-001`

Instrument: P11 `corr4_instrument/intake_derivations_v3.py` at `490ccdd...`.

Independent checks: all 10 final pins resolve, are substantive and are ancestors of declared branches; unresolved-pin, prompt-pin and non-ancestor controls fail closed; injected path grows union exactly 825 -> 826; run-location control returns byte-identical normalized output at union 825 from repository root and deep directory.

Full published 12-control membership: **12/12 PASS**, including `S06_P09_NEGATIVE_CLAIM_CONTROL_STANDARD.md` and `D24_P09_COST_CENTRE_LEVEL_REFINEMENT.md`. Default selection is unbounded; no `head`/`tail`/first-N bound is applied to the certified run.

Evidence: `RAW_EVIDENCE/P11_B35_FAILURE_CONTROLS.txt`, `P11_B35_RUN_LOCATION_CONTROL.txt`, `P11_B35_TWELVE_CONTROL_MEMBERSHIP.txt`.

**Status: CERTIFIED for the published B-35 control set. B-35 closure recommendation: CLOSE.** Certification does not claim semantic completeness beyond the stated selector/control contract.
