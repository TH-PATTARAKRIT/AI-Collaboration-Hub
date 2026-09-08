# 03 — GATE-03 P08 RC-05 FRESH DELTA + INDEPENDENT RUN

Timestamp: `2026-09-08T19:28+07:00`
Owner surface: P08 `ca577be42e6ba9535e1911dc0bad1dfab74a8aa8`
Verifier: ChatGPT GPT-5.6 Sol
Status: **FAIL — ARITHMETIC/PROVENANCE PASS, POPULATION PROPAGATION FAIL**

## Independent four-input execution

Final instrument:
`RC05_REPRODUCIBILITY/instrument/rc05_balance.py`

The default host restore client was 16.15 and failed closed on DB-T2. Re-execution was then performed with the installed 18.6 restore client, satisfying the published precondition.

Observed final results:
- DB-SM: **169,143** posted moves with lines / **417,700** posted lines; unbalanced = 0 at exact, `1e-7`, `1e-4`, `0.005`, computed and stored.
- DB-BK: **16 / 563**; all zero.
- DB-EV: **6 / 15**; all zero.
- DB-T2: **5 / 14**; all zero.
- parent-state disagreement = 0.

Injection controls independently reproduced:
- injected `0.01` -> non-zero at exact, `1e-7`, `1e-4`, `0.005`.
- injected `0.001` -> non-zero at exact, `1e-7`, `1e-4`, but zero at `0.005`.

Therefore the arithmetic instrument and threshold controls are capable of exposing defects and the published zero-balance result is reproduced.

## Provenance / namespace checks

- prediction commit `78f537876852ea6f20047524555fd89e90ee4c78` predates result commit `f0cf287ac9f4ad37b0c19145df4a0e396af84c13` in both ancestry and timestamp.
- prediction commit contains prediction/instruments and no run result.
- old bare `HO-01...HO-06` carrier is visibly RETIRED/SUPERSEDED.
- live producer-qualified `P08-HO-*` namespace is present.
- RC05 manifest explicitly excludes `MANIFEST.md` itself by definition and declares 7 substantive files / manifest as the 8th file on disk.

## Material propagation failure

The live Phase-S candidate handoff file:
`54_P08_CANDIDATE_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md`
contains a current `P08-HO-13` row stating the destructive boundary actor is:

`installed on all three`

The same file later corrects `P08-CONTRA-55` to **ALL FOUR FROZEN RC-05 EXTRACTS** and explicitly says four extracts are not an established deployment census.

Thus one live handoff row and its correction record disagree inside the same current artifact. This violates the required consistent propagation of the population-dependent install-state claim.

## Smallest next action

Owner: **P08**.
Correct only the current `P08-HO-13` handoff row (and any exact live duplicate found by one bounded variant sweep) to distinguish:
- four frozen RC-05 extracts = installed state measured;
- complete deployed estate = NOT established.
Preserve old three-input wording as lineage.

Do not re-run P08 research. The independently reproduced four-database arithmetic need not be rediscovered.

Recommendation: **GATE-03 FAIL — bounded population-propagation correction required**.
