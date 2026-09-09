# SA_CORR4_06 — AFFECTED INVARIANT RECLASSIFICATION

## CP-SA-C4-60 — AFFECTED INVARIANTS RECLASSIFIED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR4-PREGATE-CLOSURE-001]`
Branch: `architecture/phase-sa-corr4-pregate-closure-2026-09-09-001`
Boss: **SOLE FINAL APPROVER**

---

## 1. The distinction this file exists to hold

Master prompt §8 requires one separation to be made explicitly and never blurred:

> **`proof impossible in Phase SA because implementation/test is required`**
> is not
> **`Phase SA specification itself is incomplete`.**

CORR3's register put **all 58 at `HOLD — PROOF MISSING`** and said why: **57 have runtime truth-makers
and are unreachable at Phase SA by construction.** That is a statement about the phase, not about the
invariants, and **CORR4 does not move a single invariant to `PROVEN`.** What CORR4 can do — and what
this file does — is state, for each affected invariant, **which of the two categories its gap is now
in**, because `C4-01` and `C4-03` moved several across that line.

> **The reclassification, in one line: `6` invariants move from *the Phase SA specification is
> incomplete* to *the specification is complete and the proof is runtime*. `2` move the other way.
> `0` become proven.**

> **`C4-06-F-01`, found by independent challenge, not by me.** This line first read *"`4` … `2` move
> the other way"* while §8's checkpoint read *"`5` movements forward, `2` backward"* — **two different
> counts for one quantity in one file**, and the register carried **`7` `Δ` marks** — `MTI-02`, `-05`,
> `-17`, `-18`, `-38`, `-43`, `CF-I-03` — **while `MTI-46`'s value half, narrated in §4.6 as a second
> backward mover, carried no `Δ` mark at all.** Re-derived from the rows: **`MTI-05` is the one
> backward mover among the seven, so `6` moved forward**; adding `MTI-46`'s missing mark gives
> **`8` `Δ` marks = `6` forward + `2` backward**, which is what the register now carries. Neither published
> figure was right, and §4's prose discussed only four of the six. **The same defect class as
> `C4-02-F-06` — a total that sums while its distribution is wrong — in the file `SA_CORR4_02` claimed
> to have swept for exactly it. That claim was false and is withdrawn.**

---

## 2. The affected subset — declared, not chosen

**Only invariants materially affected by `C4-01`, `C4-02` or `C4-03` are re-run.** The other 33 are not
touched and their CORR3 dispositions stand unaltered.

| Source of the effect | Members | Count |
|---|---|---:|
| Element 10's gating set, as CORR3 defines it | `MTI-01`, `-04`, `-05`, `-17`, `-18`, `-19`, `-43`, `-45`, `-46`, `-50`, `CF-I-03` | **11** |
| Named by CORR3 as downstream of `MTI-18`'s enumeration | `MTI-02`, `MTI-38` | **2** |
| Family E — execution boundary, the subject of `C4-01` classes 4, 5 | `MTI-29`, `-30`, `-31`, `-32`, `-33` | **5** |
| The deferral-authority invariant `CF-I-02` | `CF-I-02` | **1** |
| Fail-closed and deny-by-default, tested by `C4-01` `G1` and `CF-I-03` `D8`/`D5` | `MTI-20`, `MTI-21` | **2** |
| The `AUTH` axis invariants `CF-I-03` asserts over | `CF-I-01`, `CF-I-04` | **2** |
| The cross-context door — `C4-02` `R8` and `CF-I-03`'s only exception path | `MTI-22`, `MTI-44` | **2** |
| **Affected subset** | | **25** |
| **Not affected, dispositions stand** | | **33** |
| | | **58 ✓** |

Verified programmatically: the 25 are **distinct**, and are a **subset** of the 58.

**Classification vocabulary, used exactly as the master prompt defines it:**

| Code | Meaning |
|---|---|
| **`SA-SPEC-COMPLETE`** | `PHASE-SA SPECIFICATION COMPLETE — RUNTIME PROOF DEFERRED TO PRE-TEST/BUILD TEST` |
| **`EVIDENCE-ACT-COMPLETE`** | An evidence act that Phase SA could perform has been performed |
| **`CONTRADICTED`** | Evidence contradicts the invariant as written |
| **`SA-SPEC-GAP`** | The **Phase SA specification itself** is incomplete |
| **`N/A`** | Not applicable |

---

## 3. The register

`Δ` marks a movement against CORR3. All movements are justified in §4.

| # | Invariant | CORR3 | **CORR4** | Δ | Exact position |
|---:|---|---|---|:---:|---|
| 1 | `MTI-01` | `HOLD` | **`SA-SPEC-COMPLETE`** | | Single resolved `CTX` per emitted fact. `0 of 41` functions exercised — a **runtime** count |
| 2 | `MTI-02` | `HOLD` — *unprovable until the enumeration exists* | **`SA-SPEC-COMPLETE`** | **Δ** | *"under any code path"* was unprovable because the path set was unknown. **The path set is now enumerated (13 classes).** What remains is executing it against a build |
| 3 | `MTI-04` | `HOLD` | **`SA-SPEC-COMPLETE`** | | Company never null. Bulk-reconfiguration case is a runtime case |
| 4 | `MTI-05` | `HOLD` — *"contradicted today"* | **`CONTRADICTED`** | **Δ** | CORR3 found the matrix declaring **more than one anchor** for some object types against *"exactly one context anchor"*. **A specification contradiction, not a runtime gap** — restated in the correct class rather than pooled with the runtime holds |
| 5 | `MTI-17` | `HOLD` — *"blocked upstream by `MTI-18`"* | **`SA-SPEC-COMPLETE`** | **Δ** | Enforcement beneath application code, demonstrated *"against every path class"*. **The path classes now exist.** Feasibility in a chosen technology is `MTI-CH-01`, **a Team B question and out of Phase SA** |
| 6 | **`MTI-18`** | `HOLD` — **unverifiable in principle** | **`EVIDENCE-ACT-COMPLETE`** (dependency) **+ `SA-SPEC-COMPLETE`** (property) | **Δ** | **The single largest movement in this file.** The enumeration was the one evidence act available and it is executed — `SA_CORR4_01`, 13 classes, 5 bounded gaps. **`MTI-18` is not proven**: *no unaudited bypass exists* is a property of a built system |
| 7 | `MTI-19` | `HOLD` | **`SA-SPEC-COMPLETE`** | | Context conformance control. Built-and-running is runtime |
| 8 | `MTI-20` | `HOLD` | **`SA-SPEC-COMPLETE`** | | Fail closed. `MTA-05` (session-fallback default) is now testable against a named path set |
| 9 | `MTI-21` | `HOLD` | **`SA-SPEC-COMPLETE`** | | Deny by default on read, scoped by the four-axis `AUTH` set |
| 10 | `MTI-22` | `HOLD — CONDITIONAL` | **`SA-SPEC-GAP`** | | **The register has 4 entries — 1 incomplete, 3 conditional, 0 settled.** `CF-I-03`'s only exception path and `C4-02` `R8` both depend on it. **The gap is in the specification: the door's contents are not closed** |
| 11 | `MTI-29` | `HOLD` | **`SA-SPEC-COMPLETE`** | | Every run resolves exactly one `CTX` |
| 12 | `MTI-30` | `HOLD` | **`SA-SPEC-COMPLETE`** | | Deferred run carries the authority and does not execute if it lapsed. `MTA-13` `RESIDUAL: NONE IN DESIGN` |
| 13 | `MTI-31` | `HOLD — RANK 2` | **`SA-SPEC-GAP`** | | Supplies run scoping, **not idempotency identity**. `RISK-C02`. **A specification gap, and it is element 15** |
| 14 | `MTI-32` | `HOLD` | **`SA-SPEC-COMPLETE`** | | Input snapshot requirement stated |
| 15 | `MTI-33` | `HOLD — VALUE HELD` | **`SA-SPEC-GAP`** | | Reason taxonomy `R4-Q-01` is **unanswered, Thai panel**. `0 of 78` Thai validations. **Not a runtime gap — the taxonomy does not exist** |
| 16 | `MTI-38` | `HOLD` — *part unprovable* | **`SA-SPEC-COMPLETE`** | **Δ** | Every act emits an immutable event carrying `CTX`, actor, **authority relied on**, two dates, evidence reference. **The authority-relied-on part was unprovable without the path set; it now has one.** But see `C4-01` `G3` — §4.3 |
| 17 | `MTI-43` | `HOLD` — *"first negative test cannot be constructed"* | **`SA-SPEC-COMPLETE`** | **Δ** | **The three negative forms are now constructible** — `CF3-B-03`, `-B-04`, `-B-05`. Executing them needs a build |
| 18 | `MTI-44` | `HOLD — CONDITIONAL` | **`SA-SPEC-GAP`** | | No handoff fact spans contexts; the paired-fact mechanism depends on `MTI-22`, which is `SA-SPEC-GAP` |
| 19 | `MTI-45` | `HOLD` | **`SA-SPEC-COMPLETE`** | | Eight consumers receive `CTX` and `AUTH` as mandatory, non-inferable. **The Payment half additionally needs a ruling** — recorded, not reclassified |
| 20 | `MTI-46` | `HOLD — VALUE HELD` | **`SA-SPEC-COMPLETE`** (count half) · **`SA-SPEC-GAP`** (value half) | **Δ** | Count conservation is runtime. **Value half `HOLD — ACCOUNTING COGS GAP`, undischarged by anything in this lane** |
| 21 | `MTI-50` | `HOLD` | **`SA-SPEC-COMPLETE`** | | Retention and inspectability. **`CF-I-03` §3.4 makes it a hard upstream dependency** — §4.4 |
| 22 | `CF-I-01` | `HOLD` | **`SA-SPEC-COMPLETE`** | | Four-axis `AUTH`, no axis substitutes for a wider one |
| 23 | `CF-I-02` | `HOLD` | **`SA-SPEC-COMPLETE`** | | Deferred execution resolves and re-resolves operation-type context. **But see `C4-01` `G5`** — §4.5 |
| 24 | **`CF-I-03`** | `HOLD` — *"the control **does not exist**"* | **`SA-SPEC-COMPLETE`** | **Δ** | **Falsified as stated** — `CF-I-03` is a published `SPECIFIED` invariant CORR3 itself counted. Control specification now published at test-writable granularity. **Not built** |
| 25 | `CF-I-04` | `HOLD` | **`SA-SPEC-COMPLETE`** | | Defining and acting are separate grants |

### 3.1 Tally, cross-checked against the rows above

| Class | Count | Members |
|---|---:|---|
| **`SA-SPEC-COMPLETE`** | **18** | rows **1, 2, 3, 5, 7, 8, 9, 11, 12, 14, 16, 17, 19, 21, 22, 23, 24, 25** — `MTI-01`, `-02`, `-04`, `-17`, `-19`, `-20`, `-21`, `-29`, `-30`, `-32`, `-38`, `-43`, `-45`, `-50`, `CF-I-01`, `-02`, `-03`, `-04` |
| **`SA-SPEC-GAP`** | **5** | rows **10, 13, 15, 18, 20** — `MTI-22`, `MTI-31`, `MTI-33`, `MTI-44`, `MTI-46` *(value half)* |
| **`CONTRADICTED`** | **1** | row **4** — `MTI-05` |
| **`EVIDENCE-ACT-COMPLETE`** | **1** | row **6** — `MTI-18`; **also** `SA-SPEC-COMPLETE` on its property half |
| **`N/A`** | **0** | |
| **`PROVEN`** | **0** | **unchanged, and unchangeable at Phase SA** |

**Counting rule, stated because two rows carry two classes.** `MTI-18` and `MTI-46` each appear in two
classes. **The unit is the invariant, so each is counted once in the primary class and its second class
is noted** — `MTI-18` primary `EVIDENCE-ACT-COMPLETE`, `MTI-46` primary `SA-SPEC-GAP`. On that rule:
**18 + 5 + 1 + 1 = 25 ✓**, matching the declared subset exactly.

---

## 4. The five movements, each with what actually moved

### 4.1 `MTI-18` — from *unverifiable in principle* to *unproven pending a build*

CORR3: *"`MTI-18` is unprovable **in principle** today, and is upstream of three others … the audit was
started and never finished."* The blocker was **not** the absence of an implementation. It was that
**the set over which the property quantifies was unknown**, so the proposition had no domain.

**`SA_CORR4_01` supplies the domain.** `MTI-18` now fails for the reason the runtime-blocked majority of the set fails —
**no implementation** — rather than for a reason unique to it. **That is not progress toward proof. It
is the removal of a distinction that made it look harder than the rest, and the removal is real.**

### 4.2 `MTI-02`, `MTI-17`, `MTI-38` — the three CORR3 named as downstream

CORR3 stated the dependency exactly: *"Until it exists, `MTI-02`, `MTI-17` and part of `MTI-38` are all
unprovable."* **The dependency is discharged for all three.** None is proven; each moves to
`SA-SPEC-COMPLETE`, and `MTI-38` carries a new qualification at §4.3.

### 4.3 `MTI-38` carries a specification defect the enumeration exposed

`MTI-38` requires every event to carry *"the full `CTX`, the actor, **the authority relied on**"*.
`C4-01` `G3` measured the canonical audit record: **`FDS_AUDIT` §12 lists 12 fields including
`tenant_id` and excluding `company_id`** — **1 of `MTI-D-02`'s 4 axes.**

> **`MTI-38` is `SA-SPEC-COMPLETE` as an invariant and the canonical baseline that must satisfy it is
> `SA-SPEC-GAP`.** These are two different documents and the gap is in the second. **Recorded here
> rather than by re-grading `MTI-38`**, because grading an invariant down for a defect in another
> party's artefact would misattribute it — and because the programme's own rule is that a correction
> lands on the row naming the identifier and nowhere else. **The `FDS` defect is `C4-01` `G3` and is
> carried there.**

### 4.4 `MTI-50` acquires a hard downstream, and the ordering is now fixed

`CF-I-03` §3.4 requires a **historised** grant store — the grant in force **at the act's timestamp**.
`MTI-50` is the retention invariant that makes such a store possible.

> **`CF-I-03` is unbuildable without `MTI-50` — not partially, not degradedly.** The Pre-Test Matrix
> may not schedule them in the other order. **Stated as a dependency observation; commissioning is not
> my act.**

### 4.5 `CF-I-02` is specification-complete and has a newly-found unintegrated sibling

`CF-I-02` covers *"every deferred, queued, scheduled or background execution."* `C4-01` `G5` found a
**Boss-approved cross-tenant metering pipeline** (`SAAS_CELL/22`, `/23`) and **four financial background
processes** (`/24`–`/27`) — all approved 2026-09-09, and cross-referenced to `CF-I-02`, `MTI-29` or
`MTI-30` in **0** places. The four wallet decisions contain **0** occurrences of `tenant`, `company`,
`context` or `scope`.

> **`CF-I-02`'s text already covers them** — *"every deferred, queued, scheduled or background
> execution"* admits no exception. **The gap is not in the invariant; it is that six newly-approved
> execution paths were designed without reference to it, and nothing in the corpus connects them.**
> `CF-I-02` therefore stays `SA-SPEC-COMPLETE` and `G5` is carried as a **cross-package integration
> gap**, which is a different object with a different owner.

### 4.6 `MTI-05` moves **backwards**, and so does one half of `MTI-46`

**Not every movement is forward, and this file says so where it is not.**

`MTI-05` was pooled by CORR3 among the 57 runtime holds while its own row recorded the matrix as
*"contradicted today"*. **A contradiction is not a missing runtime proof.** Re-graded to
`CONTRADICTED`: the specification asserts *exactly one context anchor per object type* and the matrix
declares more for some. **That is closable at Phase SA by an owner, and nothing in this round closes
it.**

`MTI-46`'s value half is `HOLD — ACCOUNTING COGS GAP`. **The COGS Gap is not a runtime gap** — it is an
undetermined accounting semantic. Re-graded to `SA-SPEC-GAP` on that half.

---

## 5. The line the master prompt asked to be drawn

| Category | Count | What it means for Boss |
|---|---:|---|
| **Proof impossible at Phase SA because implementation and an executed test are required** | **18 of 25** | **No further Phase SA round moves these.** Holding Phase SA generates specification, and specification is not what is missing here |
| **Phase SA specification itself is incomplete** | **5 of 25** — `MTI-22`, `-31`, `-33`, `-44`, `-46`(value) | **These are Phase SA work and none is closed by this round.** Their blockers are: an unclosed register, `RISK-C02`, an unanswered Thai taxonomy, a dependency on the first, and the COGS Gap |
| **Contradicted** | **1 of 25** — `MTI-05` | A specification contradiction, closable at Phase SA by its owner, **not closed here** |
| **Evidence act available and now performed** | **1 of 25** — `MTI-18` | The only one there ever was |

> **The honest summary for a reader who reads one line: of the 25 invariants this round touched, `18`
> are now blocked only by the phase boundary, `6` are blocked by Phase SA work that remains, and `1`
> was an evidence act and is done. `0` are proven, and `0` can be.**

---

## 6. What did not change

- **`0` invariants proven. `0` verified. `0` findings closed. `0` capabilities built. `6` vetoes in
  force, `0` discharged.** Every one of those figures is identical to CORR3's.
- **The 33 unaffected invariants** keep their CORR3 dispositions. **This file does not touch them and
  no reader may infer anything about them from it.**
- **Element 10** remains `specified, not built, not verified` — `AAS-V-01` wording, no substitute.
- **`0 of 41` functions · `0 of 13` enforcement surfaces · `0 of 52` negative access tests ·
  `0 of 8` isolation proofs · `0 of 3` cross-context register entries · `0 of 10` handoffs
  contract-compliant.** All unchanged.

## 7. Residual

1. **The subset boundary is mine.** 25 of 58 is a judgement about materiality. A challenger who thinks
   `MTI-06`, `-15`, `-41` or `-42` are affected by the enumeration has a case — they are **four of the
   five**
   blocked behind an undesigned capability — and I excluded them because **their blocker is `P-CAP`,
   which the enumeration does not touch.** Stated so the exclusion is auditable.
   **Corrected by independent challenge:** this sentence first named four identifiers and called them
   *"the five."* CORR3's set is **`MTI-06`, `-15`, `-31`, `-41`, `-42`** — and **`MTI-31` is inside my
   affected subset** (row 13), so the excluded set is **four, not five**. **The one place this file
   defended its subset boundary contained an arithmetic error, which is the worst place for one.**
2. **`SA-SPEC-COMPLETE` is a claim about a specification's *sufficiency for testing*, not its
   *correctness*.** An invariant can be completely specified and wrong. **Nothing in this file tests
   correctness**, and 18 rows should not be read as 18 endorsements.
3. **The two backward movements were found by re-reading CORR3's own row text against its own grade.**
   Neither came from new evidence. **A challenger should re-run that check over the 33 I did not
   touch** — if two of 25 were mis-pooled, the base rate over 33 is not zero.

## 8. Checkpoint

> ## `CP-SA-C4-60 — AFFECTED INVARIANTS RECLASSIFIED`
> **25 of 58 re-run · `18 SA-SPEC-COMPLETE` · `5 SA-SPEC-GAP` · `1 CONTRADICTED` ·
> `1 EVIDENCE-ACT-COMPLETE` · `0 N/A` · `0 PROVEN`.**
> **6 movements forward, 2 backward — `Δ`-marked: `MTI-02`, `-05`, `-17`, `-18`, `-38`, `-43`,
> `CF-I-03`, plus `MTI-46`'s value half. 33 dispositions untouched.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
