# P10 — RESEARCH EXIT GATE REPORT

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1
Assessed against `SMEPLUS-DR-EXIT-8C-001`, the Very Deep Research 8-Criteria Universal Exit Constitution.

**Boss alone issues the Final Decision. What follows is a recommendation.**

---

## 1. Criterion by Criterion

### `EC-01` Scope Bounded — **SATISFIED WITH A DECLARED FLOOR**
The research universe is bounded to one declared reference root, stated with its module count and the command that produced it. The mechanism population is declared as **a floor of eight, not a total**, with the pattern's false-negative modes written down. A second directory at the same build string holds a materially different module population and is recorded as a divergence.

**Corrected after `P10-R-08`.** The database surface **is** bounded: four deployed archives enumerated on a declared path set, three read, one class `C` because the host's tooling cannot open its archive format (`22_P10_DEPLOYED_EVIDENCE_CORRELATION.md`).

What remains unbounded: the runtime, UI, migration and client-side surfaces — `UNBOUNDED / NOT YET ENUMERABLE`. The remainder is not proven non-gating; see `EC-04`.

### `EC-02` Enumeration Converged — **NOT SATISFIED**
The author's enumeration was disproved by an independent challenge using a different pattern, which then disproved its own completeness in the same report. Two disciplined enumerations of one bounded surface returned different populations. That is the definition of non-convergence, and it is the fifth consecutive occurrence of this defect class in the programme.

### `EC-03` Unknown Exhausted — **SATISFIED**
Fifteen material unknowns, every one dispositioned, none unclassified. Seven are gating: five are Boss decisions research cannot resolve, two require runtime access. No blocker belonging to this scope has been routed to a later wave to conceal it — the asset-lifecycle route is explicitly assigned to the Asset programme because P10's scope is the kernel question, not the asset object.

### `EC-04` Tolerance-Zero Closed — **NOT SATISFIED**

**Deployed evidence added after `P10-R-08` bounds the realised exposure without closing the criterion.** In the two deployed databases that carry the function, zero recognition entries have ever been generated, all 44 companies hold one identical configuration (so the allocation-policy defect cannot currently diverge), and the chart of accounts is almost unshared (so the cross-company defect would most likely fail loudly today). None of that reproduces or refutes the code behaviour: reading stored data is a layer above reading source and a layer below running the system.

Two company-boundary defects are source-verified and **not reproduced by execution**:
- a company-scoped allocation policy resolved from the executing scope rather than the owning scope, reachable through the automatic posting routine even in a single-company-per-user tenant;
- a scopeless report object performing a company-scoped act, whose safer outcome depends on a chart-of-accounts configuration rather than on a control.

A tolerance-zero boundary may not be closed on an unreproduced inference, and the constitution forbids any conditional recommendation from bypassing one. Additionally the worst reachable scenario in `15` §3 is a **period-allocation misstatement produced by the system's own close control that passes every reconciliation** — a financial-integrity exposure that is characterised but not remediated.

### `EC-05` Contradiction Resolution Complete — **SATISFIED**
Nine material contradictions, all dispositioned with lineage. **Zero remain as differences of opinion.** Two are `HOLD / EVIDENCE REQUIRED` routed to the Accounting-Tax track, which is a disposition, not an omission. One is resolved as a conditional rather than as a choice, and says so.

### `EC-06` Negative Claim Controlled — **SATISFIED**
Twenty-two negative claims registered with class letters and declared boundaries, produced as a separately-tasked step. Two are class `E` and are prohibited from appearing anywhere. Three class `C` items are named as unsearched and must never be read as absences. Two of the author's drafted class `A` claims were downgraded before publication. A mechanical scan for system-wide negatives was run over every Layer 1 document.

### `EC-07` Two Consecutive Clean Independent Passes — **NOT SATISFIED**
One pass has run. It produced seven material corrections to the primary author's work — **none of which the author had found** — sixteen admitted new findings, one new material population, and one new gating contradiction. By the constitution's own definition that pass was not clean, so the count of consecutive clean passes stands at **zero**, and two are required.

### `EC-08` Final Knowledge Package Complete — **SATISFIED FOR WHAT IT COVERS**
All required artefacts exist: semantic model, three traces, five matrices, scope ownership, cross-process ownership, contradiction / negative-claim / unknown / dependency / revision registers, source-link register, evidence manifest with checksums, challenge record, AAS+ position with a decision package, PMO record, and the handoff pack. Repository, branch, commit and Jira lineage are recorded.

**Corrected after `P10-R-08`.** Stage E cross-layer correlation **was** performed, across the source layer and the deployed-database layer, and is documented in `22_P10_DEPLOYED_EVIDENCE_CORRELATION.md`. It produced one new finding and materially re-ordered the practical priority of several others.

Still missing, and declared missing: the runtime, UI and migration layers, and one deployed archive the host's tooling cannot open.

## 2. Gate Summary

| Criterion | Status |
|-----------|--------|
| `EC-01` Scope Bounded | SATISFIED, with a declared floor; database surface bounded, three surfaces still unbounded |
| `EC-02` Enumeration Converged | **NOT SATISFIED** |
| `EC-03` Unknown Exhausted | SATISFIED |
| `EC-04` Tolerance-Zero Closed | **NOT SATISFIED** |
| `EC-05` Contradiction Resolution Complete | SATISFIED |
| `EC-06` Negative Claim Controlled | SATISFIED |
| `EC-07` Two Consecutive Clean Independent Passes | **NOT SATISFIED** — count is zero |
| `EC-08` Final Knowledge Package Complete | SATISFIED for the source and deployed-database layers |

## 3. Recommendation

> **`RECOMMEND HOLD`**

Three of eight criteria are not satisfied, and one of the three is a tolerance-zero boundary. The constitution forbids advancing on volume, on elapsed time, on the number of challenges run, or on the absence of a veto — and none of those would be the reason to advance here in any case.

**What HOLD does not block.** The P10 decision package (`16` §5) is complete on its own criteria and should be released to the Boss now. Six downstream processes are waiting on rulings that no further research can produce. Holding the research gate and releasing the decision package are consistent acts, and the constitution's Stage J requires the second one.

**What lifts the HOLD.** In order of criticality:
1. **Executing** reproduction of the two company-boundary defects — the only route to closing `EC-04` either way. The database layer is now read and does not settle them.
2. A second independent pass with disjoint assignments, including the three declared-unsearched surfaces and a model-declaration scan across the whole reference root.
3. A third pass, clean, to satisfy `EC-07`'s consecutive requirement.
4. The Boss rulings on `P10-D-02` and `P10-D-05`, which are prerequisites to specifying the kernel rather than to closing the gate.

**Standing veto.** `AASP-VETO-01` prohibits implementation start on any P10 mechanism until `P10-D-02` is ruled. It is independent of this gate and is not lifted by it.

## 4. Statement on Wording

This report uses `SATISFIED` / `NOT SATISFIED` for the constitution's own criteria, and `RECOMMEND HOLD` as its terminal recommendation, which is one of the four permitted research-exit recommendations. No document in this package declares a pass, a freeze, a merge, or implementation authorisation. The session's terminal state is `READY FOR CORE ACCOUNTING RECONCILIATION`, which is a handoff state — it asserts that P10's outputs are ready to be reconciled against the peer processes, and it asserts nothing about the gate.
