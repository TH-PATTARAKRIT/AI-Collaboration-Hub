# P10 — ASSET COMPARISON MATRIX

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1

**Boss ruling honoured:** *never assume asset depreciation and deferred recognition share an implementation merely because both use schedules.* This document verifies rather than assumes — and reports that the evidence refutes **both** convenient assumptions.

---

## 1. The Two Assumptions, Both Refuted

| Assumption | Verdict | Evidence |
|------------|---------|----------|
| "They share an implementation because both spread an amount over time." | **REFUTED.** Thirteen structural axes compared; they agree on two. Not one line of scheduling, day-count or rounding code is shared. | §2 |
| "They are semantically distinct, because this product keeps them apart." | **REFUTED.** The asset object in the declared reference root is named for **both** domains, and its board computation still carries live commentary about inverting amounts for deferred revenue. They were one engine in this product line. | `E-P10-049` |

The second refutation was produced by independent challenge, not by the primary author, and it is the more important of the two because it removes the easiest justification for Option A.

## 2. Structural Comparison

| # | Axis | Asset depreciation | Deferral | Same? |
|---|------|--------------------|----------|-------|
| 1 | Persistent schedule object | yes — a stateful object plus a board of entries | **none** | no |
| 2 | Schedule is recomputable | yes, destructively for unposted entries | only by tearing down the source document | no |
| 3 | Event identity | entry carries the object link and a period beginning date | **none** | no |
| 4 | Entry-type marker | six-valued, stored | two-valued, computed from a link | no |
| 5 | Period grid | months or years, configurable | calendar months, fixed | no |
| 6 | Grid anchor | fiscal year, for one prorata mode | civil calendar, always | no |
| 7 | Day-count conventions | 30/360 or true calendar, separate implementation | 30/360, actual, or full-month, separate implementation | **no — same conventions, different code** |
| 8 | Residue absorption | end-of-life adjustment against the residual | forced into the last period (validation path) or plugged to the control account (grouped path) | no |
| 9 | Termination condition | **value** — the loop ends when the residual is zero | **count** — the loop ends when the periods are exhausted | no |
| 10 | In-flight modification | pause, resume, revalue, change duration, dispose | none | no |
| 11 | Catch-up on modification | yes — a stub entry cut at the modification date | validation path: none · grouped path: cumulative-to-date, structurally | **partly** |
| 12 | Lock-date guards of its own | yes, on mutation and on disposal | grouped path only | no |
| 13 | Foreign currency | cannot — the object's currency is tied to the company's | cannot — the generated lines carry no currency at all | **yes, by different mechanisms** |

Agreement: axis 13, and half of axis 11. Everything else differs.

## 3. Where the Difference Is Load-Bearing

**Axis 9 is the deepest difference and the one a kernel must respect.** Depreciation terminates on *value* — it runs until the carrying amount is consumed, so a change to the amount changes the number of periods. Deferral terminates on *count* — the window fixes the periods, so a change to the amount changes the amount per period. These are two different recurrences and they cannot be expressed as two settings of one loop without one of them acquiring behaviour it must not have.

**Axis 3 is the difference that costs the most.** Depreciation can answer "why this amount on this date?" in two hops. Deferral cannot answer it at all. That is not a semantic difference between the domains — it is a quality difference between two implementations of the same requirement.

**Axis 7 is the difference that is not a difference.** Both implement a 30/360 convention. They implement it twice, in different code, with different normalisation. Nothing about depreciation requires a different 30/360 from deferral's 30/360. This is duplication producing divergence risk, and it is the clearest candidate for kernel ownership.

## 4. The Prior Asset Round, Carried Forward Without Re-Derivation

From `SMEPLUS-26-09-04-ASSET-DEEP-L1-L6-001`, cited not re-derived:
- the asset engine's two day conventions differ by up to **8% in a February month** while **annual totals agree within 0.05%**;
- the project's legacy Thai daily method and the standard calendar mode are numerically equivalent within `0.03 THB` per period;
- the remedy for a wrong convention is a setting, not a rebuild.

**Transfer to P10:** the deferral mechanism uses the same 30/360 family, so the same detection blindness applies — **an incorrect deferral allocation setting is invisible to annual reconciliation.** Combined with the paired-defect property in `03` §6 (revenue and expense are the same code, so both move together and the net margin barely changes), the deferral mechanism has *two* independent reasons why a wrong setting will not be caught by ordinary review.

That is the single most important operational consequence in this matrix, and it is why `06_P10_PERIOD_RECOGNITION_MATRIX.md` §7 requires SMEsPlus to specify the allocation convention explicitly rather than inheriting a default.

## 5. What a Kernel May and May Not Take From This

| May be shared | Must stay separate |
|---------------|--------------------|
| The day-count convention library (axis 7) | The termination condition (axis 9) |
| The recognition event identity and its period (axis 3) | The object and its lifecycle (axes 1, 10) |
| The correction algebra's three outcomes (axis 11) | What a correction *means* in each domain |
| Lock-date and period-close semantics (axis 12) | The posting pattern and account derivation |
| Scope resolution | Residue policy (axis 8) — a policy slot, per domain, never defaulted |
| The separation of recognition period from posting date | Currency capability, which both currently lack and both must gain differently |

## 6. Classification

| Statement | Class |
|-----------|-------|
| The thirteen-axis comparison | `VERIFIED FACT`, bounded to reference root `RR-1` |
| "Not one line of scheduling, day-count or rounding code is shared" | `VERIFIED FACT` for the four named helper functions; class `B` for arbitrary shared utilities — the challenge that produced it declared this boundary itself |
| The prior Asset round's numeric results | `VERIFIED FACT` in that round; carried here as **prior evidence**, not re-derived |
| §5's allocation of responsibilities | `RECOMMENDATION` |
