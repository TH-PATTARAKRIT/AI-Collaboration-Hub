# P10 — EXIT-CRITERIA RECONCILIATION (EC-02, EC-04, EC-07)

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-CROSS-PROCESS-RECON-001` · Layer 1
Assessed against `SMEPLUS-DR-EXIT-8C-001`. **Boss alone issues the Final Decision.**

---

## EC-02 — Enumeration Converged

**Status: NOT SATISFIED. Delta measured.**

Convergence requires material-delta stability across rounds. This round is a fresh round over the same subject, and it produced material delta:

| New material item this round | Type |
|------------------------------|------|
| `P10-F-38` — deferral recognition attribution nets to zero | **New defect class** |
| `P10-F-39` — the silent re-date is specified, with an executed positive control | **Evidence-class upgrade** on an existing finding |
| `P10-F-40` — the tested path is unused and the live path is untested | **New finding** |
| `P10-F-41` — the deferral test suite has no attribution coverage | **New finding** |
| `P10-R-09` — the process taxonomy was mis-assigned in the parent package | **Correction to a material population** |
| `27` §4 — the event identity relocates to `P08` | **Design-position change** |

> **CORRECTED, `34` `W-25`.** Six items were offered under **one label and four different units**. Under a consistent unit: **two are enumeration items** (`P10-F-38`, `P10-R-09`); one is an **evidence re-class** (`F-39`); one is a **re-join of two parent facts** with no new search (`F-40`); one is a **sub-part** of `F-38` and has since been **withdrawn as contradicted** (`F-41`); one is a **design position** (the event-identity relocation). Counting a re-class, a position and a nested sub-finding as "material items" is the programme's own count-unit defect, committed in the paragraph that congratulates P10 for avoiding it.

**The criterion's status survives on the two genuine items and on the fresh round's twenty withdrawals; the count of six does not.**

**One count reconciled:** `P04` corrected a programme-wide figure — the commonly cited module count is an *entry* count; the installable population is smaller, and one directory is empty. P10's path-set enumeration counted **manifest files**, a third unit again. All three numbers are correct for their own unit and none is interchangeable with the others. P10 restates its population with its unit attached and cites no peer count without the peer's unit. This is the programme's standing unit-versus-population defect, avoided here rather than committed.

**What would close it:** two consecutive rounds with no new material population, finding class, gating unknown or Gate-changing contradiction. The count of such rounds is currently **zero**.

## EC-04 — Tolerance-Zero Closed

**Status: NOT SATISFIED — and now established as STRUCTURALLY DEPENDENT rather than merely incomplete.**

The parent round recorded two company-boundary defects as unreproduced inferences. Reconciliation has changed the shape of this criterion:

1. P10's tolerance-zero exposures — silent period misstatement, cross-company generation, attribution that nets to zero — all resolve into the **shared posting layer**, which `P08` owns.
2. `P08`'s own gate is **0 of 8 with 8 tolerance-zero boundaries open and none closed**.
3. `P11`'s `T0-13` — *a financial effect may not cross a scope boundary silently* — was widened by `P04-F-68` to need no tenant boundary and no hierarchy. **P10's own worst scenario is a single-company instance of `T0-13`.**

Therefore:

> **CORRECTED, `34` `W-24`. The word "cannot" is struck.**

The honest statement is: **`EC-04` is NOT SATISFIED, with obtainable work outstanding.** P10's own text named two obtainable, unobtained items in the next sentence, and a criterion cannot be *structurally* unclosable while its owner is naming work it could do. The status is unchanged; the **reason** is, and the reason decides whether anyone is obliged to do the work.

Worse, one of the two was **not** unobtained. `34` `W-34`: P10's own shipped script had already extracted the company table from every archive; the lock-date columns sat in every extract and P10 reported only the artefact's byte size. The question `P10-U-20` was routed as unanswered had been **answered and not read**.

What remains genuinely outstanding: an **executing** reproduction of the two company-boundary defects — and even that premise is untested, since database tooling and initialised data directories are present on the host and no attempt was made (`34` `W-13`). That premise is **class `C` — NOT ATTEMPTED**, not an environmental fact.

The scope observation still stands and is recorded separately: P10's exposures do resolve into a layer another process owns, and that process holds its own gate at 0 of 8. But that is a **statement about where remediation belongs**, not a licence for P10 to stop.

## EC-07 — Two Consecutive Clean Independent Passes

**Status: NOT SATISFIED. Consecutive clean count remains ZERO.**

| Pass | What it was | Clean? |
|------|-------------|--------|
| 1 | Four disjoint adversarial challenges, parent round | **No** — seven material corrections, sixteen new findings |
| — | Deployed-database correlation (`P10-R-08`) | Not an independent pass; a correction by the author after a peer's recorded lesson |
| 2 | This cross-process reconciliation | **No** — six material items (EC-02 above), including a correction to a material population |

A cross-process reconciliation is **not** an independent pass in the `EC-07` sense in any case: it reads peers, it does not re-examine P10 adversarially. It is recorded here for completeness, not counted.

**The fresh four-expert AAS-03 round required by the continuation directive:** commissioned; see `34` for its execution status and for what its outcome does and does not change. Whatever that outcome, it cannot by itself satisfy `EC-07`, because the pass immediately preceding it was not clean and the criterion requires **two consecutive**.

## Summary

| Criterion | Parent round | After reconciliation |
|-----------|--------------|----------------------|
| `EC-01` | Satisfied, floor declared; database surface bounded | Unchanged, with the count-unit reconciliation added |
| `EC-02` | **Not satisfied** | **Not satisfied**, delta now measured at six material items |
| `EC-03` | Satisfied | Satisfied; unknowns extended to `P10-U-20`, `P10-U-21` |
| `EC-04` | **Not satisfied** | **Not satisfied, and established as dependent on `P08`** |
| `EC-05` | Satisfied | Satisfied; no P10–peer contradiction found, one new internal correction dispositioned |
| `EC-06` | Satisfied | Satisfied; peer claims carried at their own class, none upgraded |
| `EC-07` | **Not satisfied**, count 0 | **Not satisfied**, count still 0 |
| `EC-08` | Satisfied for two layers | Satisfied for two layers plus the peer layer |

**Recommendation unchanged: `RECOMMEND HOLD`.** The reconciliation improved the evidence and reduced the ambiguity; it did not close a criterion, and it was not expected to.
