# P10 — COUPLED BOSS DECISION MATRIX

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D03`. **No decision is taken here.**

---

## 1. The Two Decisions, Retrieved Not Inferred

| | Decision A | Decision B |
|---|-----------|------------|
| **ID** | `P10-D-02` | `T0-13` / blocker `P11-B-16` |
| **Owner** | P10 raises; Boss decides | P11 raises; Boss decides |
| **Question, in the raiser's own terms** | May a posting constraint alter an original recognition period? | *"An accounting fact may be SILENTLY MUTATED, at any scope."* |
| **Status** | `BOSS DECISION REQUIRED` | **`HOLD — BOSS DECISION REQUIRED`** · tolerance-zero · present defect |
| **Close condition** | Select among `OPT-A`..`OPT-F` | *"Refuse **or** record an attributable trace"* — **refined**: where a mutation path has no violation to detect, **a trace is mandatory, not alternative** |
| **Scope** | Recognition entries | **Any accounting fact, at any scope** |

## 2. Why They Are Coupled

They are **not two questions**. Decision A is the recognition-domain instance of Decision B.

- B's subject is the mutation of an accounting fact without refusal or trace.
- A's subject is the mutation of a recognition period by a posting constraint.
- A recognition period is an accounting fact; a posting constraint is a mutation trigger.

**Every answer set that satisfies B constrains A, and no answer to A can contradict B without reopening B.**

## 3. Dependency Direction

**B governs A.** B is the general boundary; A is a domain application of it.

- If B is adopted, A's admissible set is reduced to the options that satisfy B's refined condition — which, per `39` §4, excludes `OPT-A` and excludes `OPT-B` standing alone.
- If B is rejected, A is unconstrained by B and **all six options remain**, to be chosen on domain grounds.
- If B is adopted **in a narrower form** than the refined condition, A's admissible set changes accordingly, and P10 must be re-consulted rather than assumed.

**A does not govern B.** A ruling on A cannot settle B, because B reaches accounting facts P10 does not own.

## 4. Can Either Be Decided Alone?

| Question | Answer | Reason |
|----------|--------|--------|
| Can **A** be decided without **B**? | **Technically yes, governance-wise no.** | A ruling on A taken before B would either pre-empt B for the recognition domain, or be reopened when B is ruled. Both are worse than deciding them together |
| Can **B** be decided without **A**? | **Yes.** | B is the general boundary and stands on its own. A then follows, with its admissible set determined |
| Should they be decided together? | **Yes, and B first if they must be sequenced.** | This is P10's recommendation, not a decision |

## 5. Decision Truth Table

`OPT-A` = permit silently · `OPT-B` = refuse · `OPT-C` = permit + queryable trace · `OPT-D` = full separation · `OPT-E` = lock exception · `OPT-F` = chatter trace

| # | Decision B | Decision A admissible set | Valid? | Consequence |
|---|-----------|---------------------------|--------|-------------|
| 1 | **Adopt `T0-13`, refined** | `OPT-C`, `OPT-D`, `OPT-F`, `OPT-B`+`OPT-F`, `OPT-E`+`OPT-F` | Valid | Trace mandatory on the lock-free path. `OPT-A` excluded; `OPT-B` alone excluded |
| 2 | **Adopt `T0-13`, unrefined** (*refuse or trace*) | adds `OPT-B` alone, `OPT-E` alone | **Valid but incomplete** | The lock-free path stays live and the boundary reads as met. This is the failure the refinement exists to prevent |
| 3 | **Reject `T0-13`** | all six | Valid | A decided purely on domain grounds. `OPT-A` fully available |
| 4 | **Defer `T0-13`** | all six, none eliminable | Valid | **This is the current state.** A cannot be closed; P10 holds |
| 5 | Adopt `T0-13` **and** choose `OPT-A` | — | **Invalid** | Direct contradiction |
| 6 | Adopt `T0-13` **and** choose `OPT-B` alone | — | **Invalid under the refined condition** | Leaves the lock-free path live |
| 7 | Reject `T0-13` **and** choose `OPT-C`/`OPT-D` | — | Valid | Permitted; P10 would still recommend it |

**Rows 1 and 3 are the two coherent end states. Row 4 is where the programme is today. Rows 5 and 6 are the combinations a coupled presentation prevents and a sequential one does not.**

## 6. Third Decision in the Neighbourhood — declared, not coupled

> **CORRECTED, `34` `W-39`. `D-5` is COUPLED, by this document's own criterion.**
>
> §2 defines coupling as *"every answer set that satisfies B constrains A"*, and §3 as *"if B is adopted, A's admissible set is reduced"*. This section then concedes that **`OPT-D` cannot be scoped before `D-5`** — that is, one outcome of `D-5` removes `OPT-D` from A's admissible set. **By P10's stated criterion that is coupling.**
>
> It is confirmed operationally: `AASP-VETO-01` lifts only when **both** `D-5` **and** `P10-D-02` are taken, so a ruling on A alone changes nothing on the ground.

`D-5` — *the accounting-event identity: introduce a layer-3 event object, or not.* **Coupled.** It gates `OPT-D` and P10's kernel question. `OPT-A`, `OPT-B`, `OPT-C`, `OPT-E` and `OPT-F` can be ruled without it; `OPT-D` cannot.

**The Boss faces THREE coupled decisions, sequenced `T0-13` → `D-5` → `P10-D-02`.** The earlier claim that there were two coupled and one adjacent is withdrawn.

**And a fourth is adjacent:** `D-12` — whether a company hierarchy may span a tenant boundary. The peer's register states `T0-13` *"stands whatever the Boss rules on `D-12`"*, so it does not constrain A, but it shares `T0-13`'s subject matter and the Boss should not meet it cold. It appears nowhere else in this package — `34` `W-40`.

## 7. What P10 Asks For

> Present **`T0-13` / `P11-B-16`** as a **programme-wide tolerance-zero ruling in its own right**, then **`D-5`**, then **`P10-D-02`** — three coupled decisions in that order — using the truth table in §5, with `OPT-A` **present in the option set** and marked *conditionally excluded pending `T0-13`*.
>
> **CORRECTED, `34` `W-41`.** The earlier request was to present `T0-13` *"as the second half of a P10 decision"*. **`T0-13` governs at least three domain instances at their owners' current heads**, only one of which is P10's. Presenting a programme-wide boundary as half of one process's decision understates whom the ruling binds — the same shape of error as the breach this round exists to repair, one level out.
>
> P10 also records, from the raiser's own revision log, that **`T0-13` carries a recorded defect in its own derivation**: it was scoped from the occasion that prompted it rather than from the register that already generalised it, and *"the owed enumeration was never performed"*. The Boss should see that beside the boundary — `34` `W-42`.

`BOSS DECISION REQUIRED AT FINAL GATE.`
