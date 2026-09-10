# PT-03 — PROCESS SEMANTIC AND CONTROL MATRIX

## `CP-PT-03 — PROCESS OBLIGATIONS TESTABLE`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `a33ba444`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **Map the Phase S/SA process obligation. Do NOT redesign it.**
> **`0 of 22` verified · `EC-04` `0/3` · `6` vetoes in force · `0` improvements made because this is a checkpoint.**

---

## 1. Result

| | |
|---|---|
| Dimension instrument adopted | **`SA_CORR5_10` `9`-dimension vocabulary** — `SEM`·`IN`·`OUT`·`RT`·`IC`·`AC`·`TC`·`ID`·`AU` |
| Dimension cells | **`22 × 9 = 198`** ✔ |
| `C` complete · `B` Boss election · **`G` SMEs Core/PMO/doc-owner gap** | **`185` · `13` · **`0`** |
| `S` statutory-hold markers | **`9` — *inside* cells, NOT a fourth partition** |
| Pre-Test readiness | **`10 WRITABLE` · `12 GATED`** |
| Runtime proof required | **`22 of 22` = `Y`** — no implementation exists |
| Named controls in `SA17` §3 | **`11`**, all identifiers resolve (positive + negative control fired) |
| **Material findings** | **`1`** — `PT03-F-01` |
| Apparent arithmetic defects tested and **refuted** | **`1`** — `PT03-N-01` |
| This checkpoint's own instrument errors, found and reported | **`1`** — §8 |
| Process obligations **redesigned by this checkpoint** | **`0`** |

---

## 2. The instrument — Phase SA's own dimension vocabulary, adopted by pointer

**Not invented here.** `SA_CORR5_10_22_SCENARIO_FINAL_RECONCILIATION.md` §2, verbatim:

| Code | Dimension | `C` means |
|---|---|---|
| **`SEM`** | Semantic completeness | the business fact **and its accounting meaning** are stated |
| **`IN`** | Input completeness | every required input is **named with an owner** |
| **`OUT`** | Output completeness | every emitted fact **and its consumer** are named |
| **`RT`** | Routing completeness | the flow reaches Inventory / Manufacturing / Purchase **as the law requires** |
| **`IC`** | Inventory convergence | Stock Truth reconciliation is stated |
| **`AC`** | Accounting convergence | Financial Truth reconciliation is stated |
| **`TC`** | Tenant/Company contract | `XMC-C-D1` + `HF-CTX-*` + `G1`/`G3`/`G5` |
| **`ID`** | Idempotency contract | `E15-A1`, `XMC-C-A6`…`A9`, `A14` |
| **`AU`** | Audit / control | `AUD-C`, `CF-I-03`, `CF-I-03R`, named controls |
| `RP` | Runtime proof required | **always `Y`** — no implementation exists |
| `PT` | Pre-Test readiness | `WRITABLE` — a case can be written now · `GATED` — writable only after a **named Boss election** |

**Grading law, verbatim:** *"A `G` in any dimension fails the target. A `B` is a genuine Boss election
(category 6). An `S` is a statutory evidence hold, **not a Phase SA gap**."*

> **This vocabulary maps one-to-one onto the master prompt's own required axes** —
> `INPUT → PROCESS → OUTPUT → DOWNSTREAM ROUTING → NEXT MODULE INPUT` (`IN`/`SEM`/`OUT`/`RT`), the
> accounting and inventory consequences (`AC`/`IC`), tenant and company (`TC`), identity and idempotency
> (`ID`), and audit/control (`AU`). **Adopting it avoids inventing a competing axis over the same rows.**

---

## 3. The `198` cells — measured

| Measure | Value | Basis |
|---|---:|---|
| Cells | **`198`** | `22 × 9` |
| `C` | **`185`** | derived `198 − 13` |
| `B` | **`13`** | `AC` on rows 1,2,3,4,5,6,8,9,16,17 (**10**) · `AU` on rows 5,10 (**2**) · `OUT` on row 18 (**1**) |
| **`G`** | **`0`** | **no SMEs Core / PMO / document-owner gap in any dimension** |
| `S` | **`9` markers** | rows 1,2,3,4,5,6,9 (inside `B`) · rows 13,19 (inside `C`) |

**`185 + 13 = 198`** ✔ — the true partition.

**Distinct rows carrying at least one `B` cell: `12`** — `{1,2,3,4,5,6,8,9,10,16,17,18}`. Row **5** carries
**two** (`AC` and `AU`), which is why `13` cells sit on `12` rows.

**Internal cross-check that the register passes:** the `12` `B`-cell rows are **exactly** the `12` rows
the §4.1 tally independently lists as `SA MATERIAL GAP` — `1,2,3,4,5,6` (`JT-04`) · `8,9` (`JT-05`) ·
`10` (`XD1-P1`) · `16,17` (`B-6`) · `18` (`XMC-D-02`/`XMC-D-01`). **Two independently-derived
enumerations, identical membership.**

### 3.1 `PT03-N-01` — an apparent arithmetic defect, tested and **REFUTED**

**`SC-45` §3 reports the cells as `185 C · 13 B · 9 S · 0 G`. Summed, that is `207`, against a stated
`198`. It looks like a nine-cell overcount.**

**It is not.** The register's own column header reads **`S` (inside a cell)**, and §2 grades `S` as *"a
statutory evidence hold, **not a Phase SA gap**"*. **`S` is an annotation carried *within* a `C` or `B`
cell, not a fourth disjoint class** — evidenced by the enumeration itself: rows 1,2,3,4,5,6,9 carry `S`
**inside `B`**, rows 13,19 **inside `C`**.

| | |
|---|---|
| Verdict | **NOT A DEFECT** |
| Why published | `185 + 13 + 9 = 207 ≠ 198` is the **first** arithmetic a challenger will do. The refutation is recorded so the false finding is not manufactured, **and so the refutation itself can be attacked** |
| Residual caution | **`SC-45` prints the four figures in one row without the *"inside a cell"* qualifier its source carries.** The qualifier is load-bearing and travels only in `SA_CORR5_10` — a **presentation** weakness in the summary, not an arithmetic error |

---

## 4. Pre-Test readiness — the `PT` column

| `PT` value | Count | Meaning |
|---|---:|---|
| `WRITABLE` | **`10`** | scenarios `7, 11, 12, 13, 14, 15, 19, 20, 21, 22` — a test case can be written **now** |
| `GATED` | **`12`** | scenarios `1,2,3,4,5,6,8,9,10,16,17,18` — writable **only after a named Boss election** |
| **Total** | **`22`** ✔ | |
| `RP` (runtime proof required) | **`22 of 22` = `Y`** | **no implementation exists** — this does not vary |

> **`WRITABLE` is the weakest possible claim and must not be read as anything more.** It means *a test
> case can be written*. It does **not** mean built, proven, verified or compliant — `SA15`'s mandatory
> reading rule, carried unchanged. **`10 WRITABLE` and `0 VERIFIED` are both true simultaneously.**

---

## 5. `PT03-F-01` — MATERIAL: the `0` that is ownership-scoped

### The claim as it travels

The carry-forward states, and this session reproduced at `PT-00` §4:

> **`MATERIAL PHASE-SA GAP = 0`** · *"Phase SA SMEs Core-owned specification gaps = `0` at handoff"*

### What the source register actually says

`SA_CORR5_10` §4.1, the aggregate the figure derives from:

| Aggregate | n |
|---|---:|
| `SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED` | **`10`** |
| `SA-SPEC COMPLETE / PRE-TEST READY` | **`0`** *(no implementation exists)* |
| **`SA MATERIAL GAP — EXACT GAP`** | **`12`** |

**Twelve of the twenty-two scenarios carry an exact, named, material gap.** The reconciling finding
`C5-10-F-01` states the qualifier in full:

> *"Material Phase SA gaps **owned by SMEs Core / PMO / document owner** across the 22: `0`"* — and
> *"Twelve scenarios remain `SA MATERIAL GAP`, and **every one names a Boss election**."*

### The defect

**The `0` is true only under its ownership qualifier, and the qualifier does not always travel with it.**
`SC-45` §4's six-way table prints **`MATERIAL PHASE-SA GAP` | `0`** with the twelve relocated to a
separate `BOSS ELECTION REQUIRED` row — coherent **within that table**, but the row itself carries **no
ownership qualifier**. Read alone, *"material Phase SA gap = 0"* directly contradicts
*"`SA MATERIAL GAP — EXACT GAP` = `12`"* in the register beneath it.

**Two readings, only one of which is true:**

| Reading | True? |
|---|---|
| *"`0` gaps exist across the 22"* | **FALSE** — `12` exist, each named |
| *"`0` gaps are owned by SMEs Core / PMO / the document owner; all `12` are Boss elections"* | **TRUE** |

### Why it is material

**`8C-CLARIFICATION-01` clause 5 turns on exactly this distinction** — a current-scope **specification**
gap may not be carried into Pre-Test. The clause is satisfied **only** under the second reading. Under
the first, the figure would be asserting something stronger than the evidence supports, and the twelve
would be invisible to anyone reading the headline.

### Disposition

| | |
|---|---|
| Status | **RECORDED — the underlying evidence is CORRECT; the risk is in transmission** |
| Nothing is re-graded | `12` remains `12`; `0` remains `0`; **`0` cells move** |
| Binding on this session | **every downstream citation of this `0` in `PT-04`…`PT-16` MUST carry the words *"owned by SMEs Core / PMO / document owner"*.** The bare form is prohibited |
| Routed to | `PT-13` (falsification) and `PT-14` (B-7) — **a challenger should test whether this session obeyed its own rule** |

---

## 6. The `11` named controls the Pre-Test Matrix must exercise

**Source: `SA17` §3, carried verbatim in substance. Every identifier was tested for resolution.**
**Instrument:** `grep -rlF` over the `6`-directory Phase SA path set (`192` files).
**Positive control `BD-ACC-01` → `93` files (fires). Negative control `qxvz-no-such` → `0`.**

| # | Control obligation | Identifier(s) | Resolves | Testability now |
|---:|---|---|---:|---|
| 1 | **Approval *occurrence* recorded, not only assigned** | `XD-03` | `13` | `PTE-3` — the measured *"`0 of 27,874` rows"* is **historical and generation-qualified** |
| 2 | A cross-module **auto-created** document meets the **target** module's control floor | `SA03-F-02`, `XMC-C-D3` | `13`, `8` | `PTE-3` |
| 3 | Every accounting-determining constraint holds on **non-interface write paths** | `SA11-F-02` | `5` | `PTE-3` |
| 4 | **A period lock binds the entry, not the path** | `ND-07`, `XMC-C-A15` | `7`, `8` | `PTE-3` — see `PT-08`; this is the SMEsPlus determination answering the two lock-defeat paths |
| 5 | A reservation **survives an adjustment** | `ND-05` | `9` | `PTE-3` |
| 6 | Transfer neutrality **asserted, not configured** | `SA06-F-05` | `8` | `PTE-3` — `R4-F-18`: **no independent check exists** |
| 7 | **Same-event retry is idempotent** | element 15 | — | **`PTE-3` — NOT TESTABLE UNTIL BUILT.** `SA17` §2b prohibition 2 |
| 8 | **No cross-company statutory posting** | `BD-ACC-02` | `42` | `PTE-3` |
| 9 | A non-sale reduction with **no reason class is refused** | `MTI-33` | `14` | `PTE-3` — `15` distinct classes; **labels Thai-panel, Boss commissions** |
| 10 | An act under a grant **later revoked for cause becomes `SUSPECT` without any edit** | `CF-I-03R` | `20` | **`PTE-3` — `MTI-50` must be built first** |
| 11 | A background financial process runs **one tenant at a time**, and **platform totals equal the sum of per-tenant results** | `MTI-29`, `TRG-02` | `9`, `6` | `PTE-3` |

**`11 of 11` identifiers resolve. `0` dangling control references.**

> **`11 of 11` controls are `PTE-3 EXECUTION-DESIGN READY`. `0` are `PTE-1`.** Every one asserts a
> **behaviour under conditions**, and no behaviour is evidenced by a document. **Controls 7 and 10 are
> additionally *order-gated*** — element 15 and `MTI-50` must exist before their tests may even run,
> per `SA17` §2a's dependency order.

### 6.1 The three prohibitions — carried verbatim, unweakened

1. **Nothing may be read as testing tenant isolation until an implementation exists.** `0 of 8` isolation
   proofs · `0 of 13` enforcement surfaces · `0 of 60` negative cases (52 rejection cells + `S-01`…`S-08`).
2. **Nothing may be read as testing idempotency.** The carrier is table-global; **`0 of 13,814` rows carry
   a deduplication key**; *"a test over that population returns clean and means nothing."*
3. **Nothing may be read as testing a cross-module join.** Element 15 is the join key; specified, not built.

> **Prohibition 2 names the precise hazard this whole phase exists to avoid: a test that returns clean
> and means nothing.** It is the reason `PT-10` classifies rather than scores.

---

## 7. Process obligations: prohibited transitions, reversal, audit

**Mapped, not redesigned.**

| Obligation | State | Source |
|---|---|---|
| Reversal is **a new event referencing the original** | **ESTABLISHED** | `BD-ACC-01`; `XMC-C-A8`/`A9` |
| Reversal **value basis** | **Boss election `JT-05`** — original vs current cost | `SC-45`; `09_JT05` |
| Correction after a completed movement | **the ONLY route is a return**; the corrected-entry link **does not exist** | `X-11` |
| Cancellation before physical execution | design resolved (`SA_CORR3_01`); **`AU` cell is `B`** — Boss election `XD1-P1` | `SA_CORR5_10` row 10 |
| Never-mode remainder cancellation | **leaves no document trail** → `XMC-C-D5` | `X-07` |
| Period lock | binds **the entry**, not the path (`ND-07`) | §6 control 4 |
| Adjustment vs reservation | an adjustment **can silently reduce a reservation** | `X-12` |
| Approval on adjustment | **mechanism absent** | `X-12` |
| Audit lineage | `AUD-C`, `RT-AUD-01`…`-09` | runtime family |

**`0` of these were altered by this checkpoint.**

---

## 8. This checkpoint's own instrument error — `1`, reported

| | |
|---|---|
| What | An `awk` field-index walk over the dimension columns reported `B` cells on rows `{1..9,16,17,18}` |
| Error | **Field indices off by one.** Field 3 is the **scenario name**, not the first dimension |
| Consequence | **one false positive** — row `7` *"**B**ackorder"* matched on its own name; **one false negative** — row `10`'s `B` sits in the `AU` column at the edge of the scanned range |
| How caught | the result **disagreed with the register's own explicit enumeration**, and the two rows were then read directly |
| Corrected | `B` cells = **`13` over `12` rows** `{1,2,3,4,5,6,8,9,10,16,17,18}` — the register's figure, cross-checked against its independent §4.1 tally |

> **A scenario named *"Backorder"* is enough to corrupt a column scan.** The register's own enumeration was
> right and this checkpoint's re-derivation was wrong — **so the published figure is the register's, and
> the re-derivation is reported as the error it was** rather than quietly dropped.

---

## 9. Checkpoint

> ## `CP-PT-03 — PROCESS OBLIGATIONS TESTABLE`
>
> **`9`-dimension instrument adopted from Phase SA rather than re-invented · `198` cells: `185 C · 13 B ·
> 0 G`, the `13 B` cross-checked against an independently-derived `12`-row gap list with identical
> membership · `10 WRITABLE` / `12 GATED`, `22 of 22` `RP = Y` · `11 of 11` named controls resolve, and
> **all `11` are `PTE-3` — `0` are provable by document**, `2` additionally order-gated · the three
> prohibitions carried unweakened.**
>
> **`PT03-F-01` MATERIAL: *"`MATERIAL PHASE-SA GAP = 0`"* is TRUE ONLY under its ownership qualifier —
> `12 of 22` scenarios carry an exact named gap, every one a Boss election. The bare form is now
> PROHIBITED in every downstream citation by this session, and a challenger is invited to test whether
> this session obeyed its own rule.**
>
> **`PT03-N-01`: `185+13+9=207≠198` REFUTED — `S` is an annotation inside a cell, not a fourth partition.**
> **`1` of this checkpoint's own instrument errors reported (§8). `0` process obligations redesigned.
> `0` classifications improved. `0 of 22` verified.**

Next checkpoint: `PT-04 — Output / Consumer Contract Matrix`.

No Evidence = No Progress. Never Skip Gate. Truth over Pass. Do not improve classifications because it is a checkpoint.
Boss remains the sole Final Approver.
