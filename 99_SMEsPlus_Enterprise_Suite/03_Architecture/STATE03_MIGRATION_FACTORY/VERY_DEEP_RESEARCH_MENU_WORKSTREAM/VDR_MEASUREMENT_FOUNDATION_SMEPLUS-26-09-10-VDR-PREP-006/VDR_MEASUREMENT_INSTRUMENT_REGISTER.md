# VDR_MEASUREMENT_INSTRUMENT_REGISTER.md
# Seven instruments, their inputs, their failure modes, their validators

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 06.

---

## 1. Register

| ID | Name | Input fields | Expected output | Known failure mode | Author | Independent validator | Status |
|----|------|-------------|-----------------|--------------------|--------|----------------------|--------|
| **INS-01** | Source Presence | `source_pointer` | `SOURCE_RESOLVED` · `SOURCE_FILE_ONLY` · `SOURCE_UNRESOLVED` | it measures **file length, not entity location**; no containment to the declared root; a stale pointer still resolves | VDR | SMEs Core F | **CERTIFIED WITH NON-CRITICAL LIMITATION** |
| **INS-02** | Runtime Observation | `observed_on` | `OBSERVED` · `ABSENT` | it counts **tokens**, never validating a deployment name or de-duplicating | VDR | SMEs Core F | **CERTIFIED WITH NON-CRITICAL LIMITATION** |
| **INS-03** | Four-Way Classification | `source_pointer`, `observed_on` | `BOTH` · `SOURCE_ONLY` · `RUNTIME_ONLY` · `NEITHER` | **100.00% redundant** with a column the pipeline already wrote; agrees with INS-01/02 by construction | VDR | SMEs Core F | **REJECTED** |
| **INS-04** | Exclusion Legitimacy | *declared 7 fields; **reads 1*** | `NA_ACCEPTED` · `NA_REJECTED` · `IN_POPULATION` | **single-valued on 24,553 of 24,553**; fails in both directions; 1 of 9 prohibited phrases exercised | VDR | SMEs Core F | **REJECTED** |
| **INS-05** | Cancel / Reverse Path | `identity` | `CANCEL_PATH` · `REVERSE_PATH` · `NO_EDGE_PATH` | **46–48% false negatives · 8.9–40.8% false positives · 81.8% of firings land on non-code identities** | VDR | SMEs Core F | **REJECTED** |
| **INS-06** | Contradiction | `dim_state`, `rv_state`, `fallback` | `CONTRADICTION` · `FALLBACK_FLAGGED` · `CONSISTENT` | **single-valued on 24,553 of 24,553**; one-directional; loses a co-occurring fallback | VDR | SMEs Core F | **REJECTED** |
| **INS-07** | Duplicate | `identity` | `DUPLICATE_OF_<id>` · `UNIQUE` | **4,227 false duplicates (17.2%)** — its unit is narrower than the population's key; its verdict embeds a measurement-process identifier | VDR | SMEs Core F | **REJECTED** |

**Every instrument returns `(verdict, evidence)` — never a bare boolean — so a verdict always carries the
observation it rests on.**

## 2. The structural guarantee — **WITHDRAWN**

```
fields written by any instrument : NONE      <-- a LITERAL, computed from nothing
```

**This was not a guarantee.** The value is declared, not derived, so the assertion built on it cannot
fail. A deliberately mutating instrument was installed by an independent validator and the test reported
**ALL PASS**. Under the correct scope — *fields the measurement process wrote* — **six of seven
instruments violate the contract.** See `VDR_ANTI_SELF_REFERENCE_VALIDATION_REPORT.md`.

**No instrument mutates the item it is given.** That is not a convention; it is the property the
anti-self-reference test asserts, and it is what makes "an instrument cannot grade its own output"
checkable rather than promised.

## 3. Versions

| Artefact | Version | Note |
|----------|---------|------|
| Instruments | v1 | unchanged since first execution — **no instrument was edited to make a fixture pass** |
| Fixtures | **v3** | v1 21/24 · v2 22/24 · v3 24/24; every change was to a fixture, never to an instrument |
| Harness | v2 | one defect found by the fixtures and repaired — see §4 |

## 4. The harness defect the fixtures found

The v1 harness dispatched to the **first** instrument returning a non-neutral verdict. `INS-02`'s
`ABSENT` therefore pre-empted `INS-03`'s `SOURCE_ONLY`, and two fixtures failed.

**The instruments were individually correct; the harness ordering was the defect.** Repaired: every
instrument now runs on every item and every verdict is recorded, with no first-wins short-circuit.

> This is what fixtures are for. The failure was in the code that *combines* instruments, which no
> single-instrument test would have found.

## 5. What the register does not claim

An instrument in this register has been **built and self-tested**. It has **not** been certified until
`SMES_CORE_MEASUREMENT_INSTRUMENT_CHALLENGE.md` assigns it a status and PMO verifies that assignment.
**No dimension in this package publishes official coverage from an uncertified instrument.**
