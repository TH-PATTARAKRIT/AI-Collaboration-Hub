# 06 — `MF-01` / `MF-03` RE-VERIFICATION

## `CHECKPOINT D (part 3) — CC-F-11 NARROWED · MF-03 RE-CLASSIFIED WITHOUT AN UNBUILT CONTROL`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-RECOVERY-NEWSESSION-001]` · Boss: **SOLE FINAL APPROVER**

---

## 1. `MF-01` — valuation tested independently under all three ruled methods

**`BD-ACC-03B` rules `Standard | Average | FIFO`, authority Product Category — verified at primary text.**

| Method | Does a valuation rule reach a certified opening balance? | Ground |
|---|---|---|
| **`Standard`** | **YES** | value is a **policy attribute of the product**, not a function of a movement's carried cost. `SA_CORR3_03` L178 states the same mechanism from the other side: *"under standard costing, work-centre cost **never enters** finished-goods value"* |
| **`Average`** | **NO — not without an input** | an average requires a population of valued receipts. An opening balance **is** the first population; its value must be **supplied**, not computed |
| **`FIFO`** | **NO — not without an input** | FIFO requires layers with costs. Opening layers must be **supplied** |

### 1.1 `B7-F-09` — `CC-F-11`'s universal clause is **DISPROVED**

| Clause | Verdict |
|---|---|
| *"`MF-01` creates value with no purchase and no movement"* | **STANDS** |
| *"**Every** valuation rule in the corpus binds value to a **movement** … so **no existing rule reaches** `MF-01`"* | **FALSE** — `Standard` reaches it |
| *"the counterpart account is undetermined"* | **STANDS — and is the correct residue** |

> **The universal clause travelled on the strength of the well-evidenced half beside it.** This is the
> programme's recorded **unmeasured-second-clause** defect: a finding and its consequence clause are two
> claims, and the sound half makes the other feel safe. **Narrowed to the counterpart account (`CORE-06`).**

### 1.2 `MF-01` — the six properties §6D requires

| Property | Determination |
|---|---|
| **Value creation** | **YES** — value enters without a purchase |
| **Stock movement** | **NO** — quantity enters without a movement |
| **Migration event** | **YES** — element `14` batch identity; `HX-24`, the only **dual-target** handoff |
| **Counterpart account** | **UNDETERMINED — `CORE-06`, OPEN** |
| **Reconciliation** | certified extract ↔ opening position; **`0` proven** |
| **Historical semantics** | the **cutover date**, not the system date |

**`5 of 6` determined · `1` open.**

---

## 2. `MF-03` — re-derived **without** citing an unbuilt control

### 2.1 `B7-F-10` — the prior exclusion was defective

`17_` §2 excluded `MF-03` because it *"adds ZERO quantity"* and *"adds ZERO value"*, **cited to
`RT-E15-05`** — a `PTX` control with **`0 of 11` satisfied**, resting on element 15 which is **unbuilt**.

> **The zero-effect property was design intent asserted as a fact about the flow.** If replay is not
> idempotent, `MF-03` affects stock. **The exclusion was a claim about an unbuilt control.**

### 2.2 Re-classification on evidence that does not depend on element 15

| Candidate class | Test | Result |
|---|---|---|
| **`FLOW`** | does it have its own trigger, source state and destination state distinct from `MF-01`/`MF-02`? | **NO** — replay re-executes an existing batch; **its states are the batch's** |
| **`EXECUTION MODE`** | is it a **manner of performing** another flow? | **YES** — `HX-25`/element `14` describe replay as re-running a migration package |
| `DIMENSION` | is it an attribute of a row? | **partly** — but it carries an act, not just an attribute |
| `VERIFICATION MECHANISM` | is it a test? | **NO** — `RT-E15-05` is the test **of** replay; replay is the subject |

> **`MF-03` = `EXECUTION MODE` of `MF-01`/`MF-02`** — established on **`HX-25`** and **element `14`**,
> **not** on `RT-E15-05`. **The conclusion (excluded from the flow population) is unchanged; the ground
> is now evidence rather than an unbuilt control.**

### 2.3 The residual risk that must travel

> **If replay proves non-idempotent when element 15 is built, an `EXECUTION MODE` that adds stock becomes
> a flow.** The classification is **correct on current evidence and contingent on a future measurement**,
> and is recorded that way rather than as settled.

---

## 3. Resulting populations — unchanged in number

| Register | Denominator | Reconciled | Members added |
|---|---:|---:|---|
| `IR` | **`20`** | **`14`** | `MF-01`, `MF-02` — both `NOT RECONCILED` |
| `AR` | **`30`** | **`15`** | `MF-01` — `NOT RECONCILED` |

**`IR` `14 / 3 / 3` · `AR` `15 / 14 / 1`. The denominators rose; the reconciled counts did not.**

---

## 4. Checkpoint

> ## `CHECKPOINT D (part 3) — FLOWS RE-VERIFIED`
>
> **`MF-01` tested under `Standard`/`Average`/`FIFO` independently — **`CC-F-11`'s universal clause is
> DISPROVED**; `Standard` reaches an opening balance, and the correct residue is the counterpart account
> (`CORE-06`) · `5 of 6` properties determined · **`MF-03` re-classified `EXECUTION MODE` on `HX-25` and
> element `14`, with the unbuilt-control citation removed** — same conclusion, sound ground, and the
> contingency recorded · populations unchanged: `IR 20 / AR 30`, reconciled `14` / `15`.**

