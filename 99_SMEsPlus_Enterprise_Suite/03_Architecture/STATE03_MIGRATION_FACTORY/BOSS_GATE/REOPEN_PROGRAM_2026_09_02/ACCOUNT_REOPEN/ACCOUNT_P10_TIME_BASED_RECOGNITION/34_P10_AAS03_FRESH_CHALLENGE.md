# P10 — AAS-03 FRESH EXPERT CHALLENGE (CROSS-PROCESS ROUND)

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-CROSS-PROCESS-RECON-001` · Layer 1

Four fresh challenges were commissioned with assignments **disjoint from the parent round's four**, one of them deliberately scoped at **P10's own evidence base and gate claims** — the surface every previous challenge had missed.

`Independent Review != Truth.` Every challenge finding below records whether P10 re-verified it. **Nothing was accepted on the reviewer's word alone where it changed a P10 claim.**

---

## 1. Outcome in One Line

The fresh round **disproved or materially narrowed nine P10 claims, including three the package had self-certified as class `A`, one finding, one design premise, and one statement in the gate report.** It found the `P10-R-08` defect class recurring **inside the document written to correct it**.

## 2. Findings Withdrawn or Downgraded

| # | P10 claim | Fate | P10 re-verification |
|---|-----------|------|---------------------|
| `W-01` | `P10-F-41` — "the deferral test suite contains no attribution coverage at all", class `A` | **WITHDRAWN — class `E`, CONTRADICTED.** Two dedicated attribution tests exist, one of which asserts the exact shape `P10-F-38` describes | Accepted; the claim was formed from one of the two test files and asserted over both |
| `W-02` | `P10-F-38` — "every recognition pair the deferral engine creates" writes the same attribution to both rows | **NARROWED.** True on the validation path. **False on the grouped path**, which builds two *different* distributions on different grouping keys, with a vendor test asserting that behaviour | Accepted |
| `W-03` | `P10-F-38` — the two records are "mirror images" | **REFINED.** Equal and opposite in amount, but they carry **different general accounts**, so they net at the analytic-account level and **not** under any grouping by general account | Accepted |
| `W-04` | `P10-F-38` classed `INFERENCE` for the netting arithmetic | **UPGRADED against P10's own labelling.** An executed vendor test asserts the same-distribution-on-both-rows shape. P10 under-claimed its own finding | Accepted |
| `W-05` | The mandatory-attribution gate is skipped "because these are programmatic posts / product-type rows" | **CAUSE CONTRADICTED — class `E`.** Deferral lines *are* product-type and pass that filter. The gate is inert because it requires a context key set only by user-interface buttons. **Same conclusion, wrong mechanism** — a design that fixed the stated cause would not close the hole | Accepted; this was a peer causal chain P10 adopted without deriving |
| `W-06` | `27` §2 — "three of eight mechanisms have no anchor at all" | **ARITHMETIC ERROR.** P10's own table has **four** `No` cells. Repeated in `27` §5 | Accepted |
| `W-07` | `27` §2 — the asset anchor is "the asset link, not the period" | **CONTRADICTED — class `E`.** The depreciation entry carries a populated, consumed period-beginning date, so it anchors to **asset plus period**. P10's *own parent package* `08` §2 axis 3 already said so, and `24` §7 asserted the axis table "stands unchanged" | **Re-verified from source by P10:** field defined, written at two sites, read at eight |
| `W-08` | `27` §2 — the deferral has "no anchor" | **CONTRADICTED — class `E`.** A live move-level anchor exists and is set on every generated deferral entry. What is absent is **line-level** anchoring and the **period start** | **Re-verified from source by P10** |
| `W-09` | `27` §3 — "aggregation destroys the per-fact anchor by construction", classed `VERIFIED FACT` | **CONTRADICTED — class `E`, and this was the most consequential error.** The grouped path accumulates the anchor set, sets it on the entry, and writes the full cross-product of original moves against both generated entries. **The requirement P10 posed as a design condition is already satisfied by the code P10 cited as destroying it.** What aggregation loses is per-line *amount* attribution — a weaker and different claim | **Re-verified from source by P10** |

## 3. The Evidence-Base Failure — `P10-R-08` Recurred

### `W-10` — the "unopenable" fourth deployed archive opens

P10 asserted in **six** places that the host's tooling could not read the fourth archive, and classed the question `C — NOT SEARCHED` on that basis.

A newer database tool was **already installed on the host**. P10 had run exactly one binary from the default path and inferred a boundary from its error message.

**P10 re-verified this directly: the archive opens, and its table of contents lists 26,804 entries.**

The standing lesson from `P10-R-08` was *test the evidence base before declaring it*. That formulation proved too weak. The operative rule, restated:

> **A negative about your own capability must name the tool, its version, the search for alternatives, and the command output. One tool's error message is a result, not a boundary.**

### `W-11` — the claim that overturned P10's own live-exposure argument

Reading the fourth archive changes a P10 conclusion. **P10 re-verified every figure below itself.**

| Deployed database | Companies | Any period lock set? |
|-------------------|-----------|----------------------|
| A | 44 | **0 of 44** |
| B | 44 | **0 of 44** |
| D (the "unopenable" one) | 1 | **fiscal-year, tax, sale and purchase locks all set; hard lock unset** |

`32` §3 argued the veto could not be lifted because "the deployed estate runs the path that silently re-dates, in every one of the 44 companies examined". **A lock violation requires a lock.** No lock exists in either database P10 examined, so the defect **cannot fire there**. The one deployed database where it *can* fire is the one P10 declared unreadable.

This **inverts** the parent round's live-versus-latent framing and is corrected in `22`, `29` and `32`.

### `W-12` — the declared population was never enumerated

`22` §1 declares the population as *every* deployed archive on the host, and declares the path set *enumerated, not assumed*. The shipped script globs one directory. At least three further deployed-database artefacts exist elsewhere on the volume, two of them earlier snapshots of databases already examined — a **time series** P10 did not have.

One of them carries the deployed estate's own authoritative installed-module list, which would bound a surface P10 routed as `C — NOT SEARCHED` to a named, countable set.

**This is the programme's declared-pattern-not-run defect, committed in the document that declares its own pattern.**

### `W-13` — "no runtime access" was never tested

`P10-U-01`, `P10-U-02` and `NC-20` are all routed on the premise that this session has no runtime access. Database tooling and **already-initialised data directories** are present on the host. No attempt was made. The premise is **class `C` — NOT ATTEMPTED**, not an environmental fact.

### `W-14` — the restatement-upgrade, in the two most-quoted documents

`NC-25` is scoped to **deferral** entries in one relation table. It was restated in the gate report and the handoff pack as *"zero **recognition** entries have ever been generated"* — P10's own superordinate term, covering the asset, loan and transfer mechanisms.

P10 counted the asset objects itself: **36 + 36 + 685 + 12 = 769 asset schedules across the four deployed databases.** The broad statement is false, and the narrow one is true. This is precisely the restatement-upgrade P10's own negative-claim standard names as the place where classes drift.

### `W-15` — the positive control belongs to a mechanism P10 marked "not applicable"

`28` §2's table, headed *"Current State — established, not disputed"*, lists the executed positive control **with the word "asset" removed**, while `29` §2 records that the deferral validation path has **no test at all**. The mechanism P10 owns has no executed control. Corrected everywhere: `P10-F-39` is `VERIFIED FACT` for the shared posting routine and the asset mechanism, and `INFERENCE` for the transfer to the deferral mechanism.

## 4. Reasoning Attacked and Corrected

| # | P10 reasoning | Verdict |
|---|---------------|---------|
| `W-16` | `MOVE 1` — withdrawing the recognition-event identity — rests on a peer negative over 22 roots that P10 did **not** re-derive, and that P10's own intake rule says must be read as class `C` unless among the three the peer re-ran | **UPHELD against P10.** P10 stated the rule, scoped it to two items, and did not apply it to the one that moves the design. **P10 has now partially repaired the foundation**: an executed search of the declared reference root for an accounting-event model returns **none**, against a positive control of 216 hits for the sibling pattern. That is class `A` **within one root**, not 22 — enough to support "do not author a competing identity here", not enough to support the peer's universal claim |
| `W-17` | The duplicate-identity argument, taken literally, would forbid the specialisation P10 proposes in the next sentence | **UPHELD.** Restated in `35`: the prohibition is on **two independently-authored identities for one fact**, not on specialisation |
| `W-18` | `30` §1 — four kernel elements "relocated / blocked / adopted" | **PARTLY UPHELD.** Only element 1's removal is argued from new evidence. Elements 2, 5 and 6 are **sequencing facts, not scoping facts** — a schedule of prerequisites presented as a narrowing |
| `W-19` | `24` §6 — the nets-to-zero attribution is a shared-posting-layer property | **CONTRADICTED.** The identical-attribution-on-both-legs is written by **the deferral generator itself** and, separately, by **the asset engine itself**. The shared posting layer does not construct it. So `AG-4` is **two independent mechanism-level implementations of the same wrong shape** — the strongest available fact *for* a shared allocation layer, which P10 gave away to `P08` |
| `W-20` | `30` §3 — "four independent agreements" | **REDUCED TO TWO.** Two of the four are one shared code path observed by two processes, which is not independent convergence |
| `W-21` | `30` §3 — "a defect found once is a defect found everywhere" | **WITHDRAWN as a kernel argument.** It is an argument for shared **review**, which already exists and just worked. As a kernel argument it is either circular or a maintenance argument — the code-reuse ground the Boss excluded |
| `W-22` | `30` §3 — "three processes blocked on one object" | **WITHDRAWN.** It bears on `D-5`, not on whether P10's own domains share a layer |
| `W-23` | `30` §6 falsification test 2 | **ALREADY PARTIALLY FIRED, unread.** `29` §3 row 1 shows in-flight modification differing by **domain lifecycle**, not by algebra. The surviving kernel argument is narrower than stated |
| `W-24` | `31` — `EC-04` is "structurally dependent" and P10 "cannot" close it | **"CANNOT" STRUCK.** P10's own text names two obtainable, unobtained items two sentences later, and both were skipped in a round with budget to author eleven documents. Restated as **NOT SATISFIED, with obtainable work outstanding**. The status is unchanged; the reason is not, and the reason decides whether anyone is obliged to do the work |
| `W-25` | `31` — six material items evidence non-convergence | **COUNT UNIT-CONFLATED.** Two are enumeration items; one is a re-class; one is a re-join of two parent facts; one is a sub-part of another item; one is a design position. **`EC-02`'s status survives on the two genuine items; the count of six does not** |
| `W-26` | `32` — "no further evidence bears on it, the behaviour is fully characterised" | **CONTRADICTED from inside P10's own package.** `P10-U-20` records obtainable evidence that bears directly on it, and archive D contained the only deployed lock on the host. Another negative about P10's own evidence base asserted without a search |

## 5. What the Challenges Confirmed

Recorded because surviving positives are the stronger evidence class:

1. **The netting mechanism itself.** Six candidate breakers were tested — account-type filter, line-type filter, zero-amount skip, plan-level branch, sign convention, rounding — and **none breaks it**. The analytic amount is linear and homogeneous in the balance, so identical distributions on opposite balances cancel exactly.
2. **The loan anchor** is confirmed: a posted entry resolves to the exact schedule element.
3. **The accrual's transience** is confirmed: no persistable anchor, no field pointing back to the order.
4. **No accounting-event model exists in the declared reference root** — P10's own executed search, with a positive control.
5. **No prohibited verdict wording anywhere in the package**, and **no usurpation of the Boss-reserved decision**. Every occurrence of the reserved question is carried as `BOSS DECISION REQUIRED`.
6. **The intake discipline in `23` §2** — refusing the peer's unre-run class-`A` claims, refusing the peer synthesis, refusing peer counts without their unit — was assessed as the strongest part of the package. It failed only where it was **stated and then not applied** (`W-16`).

## 6. New Finding Produced by the Challenge Round

**`P10-F-42`** — the asset engine guards its attribution emission (`if a distribution exists`) with a vendor comment explaining that emitting the key unconditionally would suppress the computed default. **The deferral generator has no such guard** and always emits the key. Consequence: distribution-model defaults never apply to deferral recognition lines when the source line carries none.

Class: `VERIFIED FACT` for the code asymmetry, `INFERENCE` for the runtime consequence. Reviewer-originated; **not** independently re-derived by P10 — carried at class `B` and not used as sole support for anything.

## 7. Effect on `EC-07`

This round is **not clean** by a wide margin: nine claims withdrawn or narrowed, three of them self-certified class `A`; one finding withdrawn outright; one gate statement corrected; one new finding admitted.

**Consecutive clean independent passes: still ZERO.**

## 8. Errors the Challenges Found in P10's Own Briefs

Four again, one per challenge — the same rate as the parent round: a reference root that omitted the second module tree; line references drifting by several lines; a causal chain inherited from P10's own wrong statement; and a population framing that would have reproduced P10's bounding error one level up. The instruction to report brief errors as findings continues to earn its place in every brief.

---

## 9. Challenge 3 — The Boss-Reserved Decision. The Round's Most Damaging Result.

Challenge 3 was scoped at the one question the directive reserves to the Boss. It found that P10 **did not** decide that question — and **did** covertly decide a prior one.

| # | Finding | P10 re-verification |
|---|---------|---------------------|
| `W-27` | **P10 treated an open peer blocker as an adopted programme boundary.** `28` and `32` both asserted the tolerance-zero boundary was "adopted programme-wide" and derived from it that the status quo is excluded. The peer's own register carries it as **`BOSS DECISION REQUIRED` / `UNRESOLVED`, 0 of 13 resolved**. P10's own `23` §4 had already classed the close condition as an *adopted position, not a fact* — so the package contradicted itself in three places | **Accepted.** The elimination of the status quo is now stated as **conditional on the Boss adopting that boundary**, and the Boss is told the two decisions must be taken **together** |
| `W-28` | **P10's claim that a peer's veto is "broader and binds first" is false.** That peer's veto is scoped to its own model, implementation-only, and its text says explicitly that it does **not** block other processes. Consequence: `AASP-VETO-01` is **not** redundant — it is the only veto binding P10's implementation, and P10 narrowed it believing otherwise | **Accepted.** `32` restored to revision 3 |
| `W-29` | **An option was missed that removes the stated blocker on the trace-preserving family.** The product ships a first-class lock-exception object recording company, user, reason, validity window and the original lock date; an active exception suppresses the violation so the entry posts **at its own date**. No period object, no ledger change | **Re-verified from source by P10.** Added as Option E. Bounds recorded: the irreversible hard lock is not exception-able, and the object is absent from the older estate line |
| `W-30` | **A second missed option:** the posting routine already posts a chatter message in the branch six lines above the silent re-date. Recording the original period the same way costs nothing another process owns | **Re-verified from source by P10.** Added as Option F. It also settles that **the silence is a choice, not a limitation** |
| `W-31` | **"First open period" is not one convention.** The landing period is selected by the journal's **sequence numbering format** — a month-reset sequence lands at that month's end, a year-reset sequence lands at **31 December**. Same lock, same charge, different period | **Re-verified from source by P10.** A defensible accounting convention does not change its answer because a sequence resets yearly instead of monthly. This materially strengthens the misstatement reading over the convention reading |
| `W-32` | **P10 over-stated the positive control by one notch.** The test's stated subject is changing a computation method with draft moves before a lock; the re-dating is recorded **incidentally, while testing something else**. Accurate: *the suite records the re-dating as expected output of a test aimed elsewhere* — still decisive for "specified, not accidental", weaker than "the vendor asserts a misstatement as correct" | **Accepted** |
| `W-33` | **`P10-F-40` is falsified as worded.** A test *does* exercise generation into a locked period on the validation path — it asserts the entry count and **nothing about the dates**. The correct finding is **stronger**: the suite runs the live path under a lock and declines to assert where the money lands | **Accepted.** `29` corrected |
| `W-34` | **P10 extracted the evidence that mattered and never read it.** P10's own shipped script extracts the company table from every archive; the lock-date columns were in every extract, and P10 reported only the artefact's byte size. `P10-U-20` was routed as "obtainable and not obtained" — **it had been obtained and not looked at** | **Accepted.** This is the *executed-not-quoted* failure in its inverse form: the command ran and the column that decided the question was never printed |
| `W-35` | **A ruling scoped to the lock path would not dispose of the problem.** A peer records a **second re-dating path that fires with no lock configured at all**, triggered by a document-date change. Every option in `28` is framed around the lock | **Accepted.** Recorded as `P10-U-23` and flagged to the Boss inside the decision package |

### 9.1 Where Challenge 3 Was Itself Wrong

`Independent Review != Truth`, and this is the instance.

Challenge 3 concluded, with a positive control, that **"no deployed company has any lock date set"** across three archives — and therefore that the defect cannot fire anywhere in the estate.

**P10 verified the same columns and found the fourth archive carries four lock dates set.** Challenge 3 did not read that archive, because P10's own package had declared it unreadable — so the challenge inherited P10's bounding error one level up, exactly as the challenge itself warned could happen.

**Corrected estate position, P10-executed with a positive control:**

| Deployed database | Companies | Lock dates set |
|-------------------|-----------|----------------|
| A | 44 | none |
| B | 44 | none |
| C | 1 | none |
| **D** | **1** | **fiscal-year, tax, sale and purchase all set; hard lock unset** |

So the defect **cannot fire in three of four** and **can fire in the fourth**. Both P10's original framing and the challenge's correction of it were wrong in opposite directions.

## 10. Cumulative Result of the Fresh Round

| | Count |
|---|-------|
| P10 claims withdrawn or materially narrowed | **20** |
| Of those, self-certified class `A` before the round | 3 |
| Findings withdrawn outright | 1 (`P10-F-41`) |
| Findings strengthened by challenge | 3 (`F-38` netting; `F-40` restated stronger; `F-39` grounds widened) |
| New options discovered | 2 (`E`, `F`) |
| New defect classes | 2 (`P10-F-42`; the corrective reversal landing in a different period, now with a positive control) |
| Reviewer claims P10 verified and **corrected** | 1 (§9.1) |
| Corrections originating with the author | **0** |

**Consecutive clean independent passes: ZERO.** This round was the least clean of the three.
