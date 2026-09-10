# SMES_CORE_MEASUREMENT_INSTRUMENT_CHALLENGE.md
# Independent validation — 5 of 7 instruments REJECTED

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 09.

The validator has **no authorship stake** in any artefact it examined, ran everything in an isolated
sandbox against byte-identical copies, and verified afterwards that nothing in the package was written
to. **21 findings. All adopted.**

---

## 1. Statuses

| Instrument | Status |
|-----------|--------|
| **INS-01** Source Presence | **CERTIFIED WITH NON-CRITICAL LIMITATION** |
| **INS-02** Runtime Observation | **CERTIFIED WITH NON-CRITICAL LIMITATION** |
| **INS-03** Four-Way Classification | **REJECTED** |
| **INS-04** Exclusion Legitimacy | **REJECTED** |
| **INS-05** Cancel / Reverse Path | **REJECTED** |
| **INS-06** Contradiction | **REJECTED** |
| **INS-07** Duplicate | **REJECTED** |

**2 certified with limitation, 5 rejected.** §14: *no rejected instrument may produce official coverage.*

## 2. The critical findings, each reproduced here before adoption

### The anti-self-reference test cannot fail
`WRITTEN_FIELDS` is an empty literal; the assertion is empty by construction. A deliberately mutating
instrument was installed and **the test reported ALL PASS**. Reproduced. Full account in
`VDR_ANTI_SELF_REFERENCE_VALIDATION_REPORT.md`, which is rewritten as a **FAILURE**.

### Six of seven instruments read fields the measurement process wrote
The contract was scoped to *instruments* writing fields; the exposure is *the pipeline* writing them.
All seven input columns are produced by the same run that grades them.

### INS-03 is 100.00% redundant with a column already written
24,553 of 24,553 rows. It re-derives `discovery` from the same two inputs the union script used to
write it — and, being a pure function of INS-01 and INS-02, it **agrees with them by construction**,
manufacturing corroboration. Reproduced.

### INS-04 and INS-06 are single-valued over the entire population
`IN_POPULATION` on 24,553 of 24,553; `CONSISTENT` on 24,553 of 24,553. **The fields they read are not
columns of the population.** Neither can fire on the artefact it is published beside. Reproduced.

### The fixture result is 24 selections, not 24 tests
The harness computes **168** verdicts and compares **24** (14.3%) against an expectation; **144 (85.7%)
are computed and discarded unchecked.** A fixture passes if *any* of seven instruments emits the expected
string. **"24 of 24" may not be cited as evidence of instrument correctness.**

### INS-04's declared inputs do not match its code
Seven declared; the body reads **one**. `INS04_exclusion({})` returns the graded verdict of **11 of the
24 fixtures** — an empty dictionary reproduces them. Those eleven "hidden / disabled / optional /
config-off / restricted must never mean excluded" fixtures do not test that the instrument *ignores*
those fields; **it cannot see them.**

### INS-05's error rates, quantified against the corpus
| | rate |
|---|---:|
| false negatives — real cancel paths whose identifier carries no token | **46.2% – 47.5%** |
| false positives — token present, method is not the path | **8.9% – 40.8%** |
| population firings landing on identities with no `::` at all — access lines, reports, views, model names | **81.8%** |

Named: the method where a transfer actually becomes cancelled returns `NO_EDGE_PATH`; a button that
merely opens a wizard returns `REVERSE_PATH`. **The programme's cancel and reverse figures rest on this
instrument.**

### INS-07 produces 4,227 false duplicates
17.2% of the population. Its unit is `identity`; the population's key is `(kind, identity)`. **Genuine
within-kind collisions: 0.** Its verdict string also embeds a measurement-process identifier — a direct
counter-example to the anti-self-reference claim.

### The agreement figure mixes three platform generations against one source tree
| basis | agreement |
|---|---:|
| as published, five deployments | **49.5%** |
| the three current-generation deployments only | **53.9%** |

**765 of the 2,783 comparable runtime-only rows (27.5%) exist only on a deployment of a different
generation from the source tree**, and are scored as method disagreement. **No version basis was
declared.** This is the largest single distortion of the published rate.

### "Logically independent" is false as written
The runtime method opens the source method's output to obtain the domain module set. Perturbing that
set moved the runtime output by **74.6%**. The two are independent in **observation** — different
evidence bases, neither derives an entity from the other — and **not independent in population**. The
agreement rate therefore has **zero power against an error in the shared scope**. A runtime-native
module set was available on all five deployments and was not used.

### The normaliser drops real matches, and its constraint branch is a guaranteed-zero join
89 of 4,948 runtime field identities and 35 of 620 model identities are misnormalised; **48 rows would
flip from disagreement to agreement** under a correct map. And **CONSTRAINT: 46 source-only, 41
runtime-only, 0 both** — the exact "perfect, artefactual disagreement" this round claimed to have fixed,
present and unremarked in a third namespace, inside the comparable denominator.

## 3. What the validator confirmed — and it matters

| | |
|---|---|
| **No instrument mutates its input** | static scan plus dynamic deep-copy diff: **zero mutation sites** |
| **No instrument was edited to make a fixture pass** | all three preserved runs reproduced **byte-identically** with the unmodified instruments, corroborated by timestamps. **The round's central claim survives adversarial reconstruction** |
| **Determinism** | two consecutive runs identical, and identical to the published result |
| **Every Hop-0 count reproduces** | 1,433 modules · 51 anchor models · 99 domain modules · 12,092 source entities · 24,553 union · 9,170 comparable · 4,537 both. The regenerated population file is **byte-identical** to the published one. Every count validated by a second command of a different shape |
| **The normaliser cannot fabricate a match** | 0 collisions in the model space, 0 in the field space |
| **Every published source pointer is correct** | all **7,695** checkable pointers land on the declaring line — *for reasons the instrument does not check* |
| **The runtime parser is generation-aware, not padded** | per-file column headers; 0 rejected rows over 714,052 lines |
| **A published zero is real** | the legacy-constraint zero re-run in three forms with a firing positive control |

## 4. One correction the validator made to this package's own narrative

The harness's inline account of the v1 fixture defect — *"dispatch took the first non-neutral verdict"* —
**is contradicted by the preserved v1 result**, which records a last-wins attribution. The harness was
not changed between v1 and v3 either. **The narrative is unsupported by the artefacts it cites**, and
the claim that "the instruments caught two defective fixtures" is loose on both counts.

**Adopted. The account is corrected, and the preserved results stand as the record.**

## 5. Constraints binding anything this package publishes

- The **"24 of 24"** fixture result may **not** be cited as evidence of instrument correctness.
- **"Logically independent"** may not be carried forward without the population-scope qualification.
- The **49.5%** agreement figure may not be cited without stating that it mixes three generations and is **53.9%** on a constant basis.
- **INS-01** may not be cited as evidence that an entity is declared at a location, nor that a pointer lies inside the declared path set.
- **INS-02** may not be cited as evidence that a named deployment exists or that its count is de-duplicated.

## 6. The validator's own declared limit

It has no preserved copy of the v1 or v2 source files — only the result files. Its confirmation that no
instrument was edited rests on reconstruction from the v3 account plus timestamps: **consistent and
mutually corroborating, and not a preserved artefact.**

**Adopted as a process requirement: preserve the source of every version, not only its output.**
