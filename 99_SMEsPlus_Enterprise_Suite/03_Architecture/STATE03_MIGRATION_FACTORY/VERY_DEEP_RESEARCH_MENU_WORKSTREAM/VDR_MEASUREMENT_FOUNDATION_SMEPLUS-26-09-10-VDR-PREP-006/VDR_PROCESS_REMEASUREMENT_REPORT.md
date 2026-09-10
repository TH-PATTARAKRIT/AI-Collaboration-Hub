# VDR_PROCESS_REMEASUREMENT_REPORT.md
# Process re-measured against the reconstructed population — 88.54% becomes 32.6%

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 12 / 18.

---

## 1. The instruction, and what it costs

§18: *"Do NOT assume the PREP-005 Process result is certified. Recalculate from the reconstructed Hop-0
Population."*

PREP-005 measured process over **1,510** process-applicable items and reported **88.54%**. The
reconstructed Hop-0 population contains **4,096 behaviours** — the entities whose process the facet
model actually reads — of which the PREP-005 instrument covered **614**.

| | |
|---|---|
| Behaviours in the reconstructed Hop-0 | **4,096** |
| Behaviours the facet model has been run over | **614** |
| **Process coverage against the reconstructed population** | **≈ 15.0% of behaviours; 1,337 of 4,096+ process-applicable entities ≈ 32.6%** |
| Against the 96% floor | **FAIL** |

**The 88.54% was not wrong. It was measured over a quarter of the behaviours that exist.**

## 2. The evidence-level distinction §18 requires

For every facet the model must distinguish **OBSERVED · DERIVED · INFERRED · UNVERIFIED · N/A**, and
*derived is not automatically equivalent to observed*. Applied to the twenty facets:

| Evidence level | Facets | Why |
|----------------|--------|-----|
| **DERIVED** — from the parsed body, deterministically | 01 Entry Point · 02 Preconditions · 03 Input Validation · 04 Business Rules · 05 Decision Branches · 06 Calculation · 07 State Transition · 08 Internal Actions · 09 Data Read · 10 Data Write · 12 Scheduler · 13/14 Cross-Module · 15 Error Handling · 16 Failure Path · 17 Retry · 18 Cancel · 19 Reverse · 20 Output | the syntax tree is an artefact outside the register, and the derivation rule is published |
| **OBSERVED** | 11 Automation | joined to the deployments' own job and server-action records, on **model and method** |
| **INFERRED** | none published | — |
| **UNVERIFIED** | the residue, per item | recorded per facet, never as N/A |

**Nineteen of twenty facets are DERIVED, one is OBSERVED, and none is inferred.** That distinction was
not drawn in PREP-005, and drawing it changes what the 88.54% may be claimed to mean: it is a *derivation*
coverage, not an *observation* coverage.

## 3. What survives from PREP-005 unchanged

- **The instrument.** Twenty facets on the syntax tree; 614 of 614 behaviours resolved exactly, 0 fallbacks, 0 parse failures.
- **The failing control that was caught.** The cancel and reverse predicates first returned a clean 0 of 614 because a word boundary cannot match inside `action_cancel`. Caught by a corpus-drawn control **before** publication.
- **The automation precision correction.** A method-name join over-counted by **81.1%**; requiring model *and* method gives 34 of 614.
- **The findings.** 87.9% of behaviours perform no arithmetic; 99.5% handle no exception; 99.2% have no retry path; data mutation exceeds state transition by roughly twelve to one.

**None of that is retracted. All of it now describes 614 of 4,096 behaviours** — and says so.

## 4. Why the instrument was not simply re-run over all 4,096

It could be, and it should be, and it was not done in this round because **the population it would run
over is not certified**: two independent discovery methods corroborate 49.5% of it. Running a good
instrument over an uncertified population would produce a number with the same defect this round exists
to eliminate — a percentage whose denominator nobody has validated.

**That is the sequencing this round enforces: certify the population, certify the instrument, then
measure. Not the other way round.**

## 5. Against the threshold

| | |
|---|---:|
| Process Coverage, reconstructed basis | **≈32.6%** |
| Floor | 96% |
| | **FAIL** |
