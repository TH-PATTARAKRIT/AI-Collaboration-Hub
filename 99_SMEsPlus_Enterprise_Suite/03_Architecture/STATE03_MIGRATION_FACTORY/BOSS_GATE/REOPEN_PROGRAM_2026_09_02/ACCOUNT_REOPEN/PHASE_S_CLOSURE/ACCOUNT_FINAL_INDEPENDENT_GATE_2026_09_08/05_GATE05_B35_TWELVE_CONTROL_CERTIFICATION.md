# 05 — GATE-05 B-35 FINAL INDEPENDENT CERTIFICATION

Timestamp: `2026-09-08T19:28+07:00`
Owner surface: P11 `490ccdd81a4fed79d36b7b9d3bbc25deedd597b4`
Verifier: ChatGPT GPT-5.6 Sol
Status: **PASS — B-35 CERTIFIED**

## Instrument reproduced

Instrument:
`P11_CENTRAL_CORE_RECONCILIATION/LAYER2_P11_EVIDENCE/corr4_instrument/intake_derivations_v3.py`

Final run at frozen peer pins produced:
- D1 = **57**
- D2 = **51**
- D3 = **823**
- UNION = **825**
- A∩B = 21; A−B = 36; B−A = 30
- full Markdown population = **10,475**
- selected = **825**
- measured complement = **9,650**
- basenames with more than one full path = **294**
- raw-substring-only extra admissions = **70**

These measurements independently exercise the repaired chronology/full-path/bounded-token/complement/unbounded-population design rather than relying on the owner's narrative.

## Full published twelve-control set

Certification premise from the prior challenge: **every artefact CORR2 was shown to have missed must return**. Independent harness loaded the final instrument, used its final frozen pins, derived the final UNION, and checked each control by its published unique filename token.

| # | Control | Expected | Observed | Result |
|---|---|---|---|---|
| 1 | `43_G02_P02_FINAL_CLEANROOM_HANDOFF` | included | 1 UNION hit | PASS |
| 2 | `D23_P09_P11` | included | 1 | PASS |
| 3 | `D25_P09_CHALLENGE` | included | 1 | PASS |
| 4 | `D26_P09_V18` | included | 1 | PASS |
| 5 | `D27_P09_EVIDENCE` | included | 1 | PASS |
| 6 | `S18_P09_P11` | included | 1 | PASS |
| 7 | `S23_P09_POST` | included | 1 | PASS |
| 8 | `37_P03_SCOPE02` | included | 1 | PASS |
| 9 | `71_P10_CORE_RECON` | included | 1 | PASS |
| 10 | `P01_S16_P11_HANDOFF` | included | 1 | PASS |
| 11 | `S06_P09_NEGATIVE_CLAIM_CONTROL_STANDARD` | included | **1** | **PASS** |
| 12 | `D24_P09` | included | 1 | PASS |

The prior defective instrument returned S06 = 0. The rebuilt instrument now returns S06 exactly once while remaining unbounded by the old fitted `TAIL=5` rule.

## Real failure controls

Independent `--controls` execution:
- unresolvable pin -> exit 3 / `UNRESOLVED` = PASS
- non-substantive prompt commit -> exit 3 / `NON-SUBSTANTIVE` = PASS
- pin not ancestor -> exit 3 / `NOT AN ANCESTOR` = PASS
- synthetic positive path -> UNION **825 -> 826**, exactly the injected path = PASS

## Working-directory independence

Independent `--run-location-control` execution from repository top level and a deep package directory:
- top-level UNION = **825**
- deep-directory UNION = **825**
- substantive output byte-identical = **TRUE**

## Certification

All mandatory material controls, including S06, passed. The rebuilt instrument enforces frozen pins fail-closed and no longer depends on invocation directory.

Known disclosed boundary: peer artefacts with filenames lacking the bounded peer token can remain outside this selector. This is a declared selector boundary, not a failure of the published twelve-control certification; it must not be converted into an absence claim.

Recommendation: **B-35 CERTIFIED**.

Dependent note: B-27 may now be reconsidered only against its own remaining preconditions; B-35 no longer blocks that reconsideration.
