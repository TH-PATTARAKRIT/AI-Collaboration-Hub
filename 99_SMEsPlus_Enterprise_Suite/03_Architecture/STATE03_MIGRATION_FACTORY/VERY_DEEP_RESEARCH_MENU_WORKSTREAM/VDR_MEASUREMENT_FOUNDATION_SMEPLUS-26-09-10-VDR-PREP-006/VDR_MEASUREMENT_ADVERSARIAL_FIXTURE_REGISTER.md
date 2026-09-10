# VDR_MEASUREMENT_ADVERSARIAL_FIXTURE_REGISTER.md
# Twenty-four fixtures, expectations fixed before execution, three preserved runs

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 07.

---

## 1. The discipline

Every fixture's **expected result was written before any instrument ran**, in the fixture file, and it
is the only place it is written. **No instrument reads the fixture file** — the harness compares; the
instruments never see the expectation. An instrument that could read its own expected answer would be
the self-reference this round exists to eliminate.

## 2. The twenty-four

| ID | Class | Expected | What it traps |
|----|-------|----------|---------------|
| FX-01 | TRUE POSITIVE | OBSERVED | declared and present |
| FX-02 | TRUE NEGATIVE | ABSENT | declared nowhere, present nowhere |
| FX-03 | **FALSE POSITIVE TRAP** | SOURCE_UNRESOLVED | a **real file** with an **impossible line** |
| FX-04 | **FALSE NEGATIVE TRAP** | CANCEL_PATH | a token separated by an underscore — invisible to a word-boundary predicate |
| FX-05 | MISSING DATA | SOURCE_UNRESOLVED | observed at runtime, no pointer at all |
| FX-06 | DUPLICATE ITEM | DUPLICATE_OF_FX-05 | one identity, two provenances |
| FX-07 | **INVALID N/A** | NA_REJECTED | a persistent model asserted to have no security surface |
| FX-08 | HIDDEN FUNCTION | IN_POPULATION | hidden must never mean excluded |
| FX-09 | DISABLED BUT PRESENT | IN_POPULATION | disabled must never mean excluded |
| FX-10 | OPTIONAL FUNCTION | IN_POPULATION | optional and uninstalled must never mean excluded |
| FX-11 / FX-12 | CONFIG OFF / ON | IN_POPULATION | a gate state must never remove an element |
| FX-13 | CONFIG ALTERNATIVE | IN_POPULATION | a third state, not a second |
| FX-14 | SECURITY RESTRICTED | IN_POPULATION | restricted must never mean excluded |
| FX-15 | STATE RESTRICTED | IN_POPULATION | state-gated must never mean excluded |
| FX-16 / FX-17 | RUNTIME UNREACHABLE · SOURCE PRESENT / RUNTIME ABSENT | SOURCE_ONLY | the four-way classification must survive an absent runtime |
| FX-18 | RUNTIME PRESENT / SOURCE PATH DIFFERENT | RUNTIME_ONLY | installed from a module with no source in the declared path set |
| FX-19 | CROSS-MODULE OWNERSHIP | IN_POPULATION | ownership elsewhere is not an exclusion ground |
| FX-20 | INHERITED MODEL | IN_POPULATION | an extension is surface |
| FX-21 | MODULE EXTENSION | IN_POPULATION | a field added by the domain to a foreign model |
| FX-22 | SILENT FALLBACK | FALLBACK_FLAGGED | a resolver that falls through must be visible |
| FX-23 | CANCEL / REVERSE | CANCEL_PATH | the plain case behind FX-04 |
| FX-24 | CONTRADICTORY EVIDENCE | CONTRADICTION | not-verified and verified on one cell |

## 3. The three runs — all preserved

| Version | Result | What changed, and to what |
|---------|--------|--------------------------|
| **v1** | **21 of 24** | — |
| **v2** | **22 of 24** | **FX-06's expected value was malformed** — a missing hyphen in the identifier it expected the instrument to echo. **The instrument was right; the expectation was wrong.** The harness dispatch defect was repaired in the same step |
| **v3** | **24 of 24** | **FX-16 and FX-17 carried fabricated source paths**, so they tested *"no such file"* rather than *"source present, runtime absent"*. **The instrument was right to refuse to call a non-existent path source-present; the fixture data was wrong.** Real paths substituted; **the expectations were not touched** |

> **Every correction across three versions was made to a fixture or to the harness. Not one instrument
> was edited to make a fixture pass.** That claim is checkable from the preserved results and the
> instrument file, and an independent validator was asked to check exactly it.

## 4. What "24 of 24" actually means — corrected by independent validation

The harness computes **168 verdicts** (24 fixtures × 7 instruments) and compares **24 of them — 14.3% —
against a stated expectation. 144 are computed and discarded unchecked.** A fixture passes if **any** of
the seven instruments emits the expected string.

**"24 of 24 PASS" is 24 selections, not 24 instrument tests, and it may not be cited as evidence of
instrument correctness.**

Worse, **11 of INS-04's 12 fixtures are reproduced by an empty dictionary** — that instrument declares
seven input fields and reads one, so the "hidden / disabled / optional / config-off / restricted must
never mean excluded" cases do not test that it *ignores* those fields; **it cannot see them.**

## 5. What the fixtures found

- **A harness defect** invisible to any single-instrument test: first-verdict-wins dispatch pre-empted the four-way classifier.
- **Two defective fixtures**, both caught by the instruments refusing to agree with a wrong expectation. **An instrument that catches its own test's error is the strongest signal available here** — and it is the reason the v1 result is preserved rather than replaced.

## 6. Adequacy — and the validator's answer

**24 fixtures for 7 instruments, and one instrument absorbs 12 of them.** That is uneven, and it means
the coverage of the *other six* rests on two fixtures each. **An independent validator was asked to find
a case each instrument would get wrong that no fixture covers**, and that question is answered in the
challenge report, not here.
