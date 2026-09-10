# PT-06 — ACCOUNTING + INVENTORY UNIVERSAL CONVERGENCE MATRIX

## `CP-PT-06 — ACCOUNTING/INVENTORY CONVERGENCE MAPPED, NOT PROVEN`

*(master-prompt checkpoint name: `CP-PT-06 — ACCOUNTING/INVENTORY CONVERGENCE COMPLETE`)*

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `e9efb6fb`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **`Accounting owns Financial Truth. Inventory owns Stock Truth.`**
> **`0 of 22` verified · `0 of 58` invariants proven · `6` vetoes in force.**

---

## 1. Result

| | |
|---|---|
| Stock-affecting flows (`IR-01`…`IR-18`) | **`14 RECONCILED` · `3 PARTIAL` · `1 NOT RECONCILED`** = `18` ✔ |
| Material business flows (`AR-01`…`AR-29`) | **`15 RECONCILED` · `14 PARTIAL` · `0 UNKNOWN`** = `29` ✔ |
| Of the `15` accounting `RECONCILED` | **`5` are `NO POSTING BY DESIGN`** — reconciled by *not* posting |
| Flows with **no** accounting semantic | **`0 of 29`** — *"None is unanswered"* |
| **Flows RECONCILED without a named open element** | **`15 of 29`** |
| Scenarios blocked on recognition-point + cost basis (el.`4`/`7`) | **`11 of 22`** |
| **Material findings** | **`2`** — `PT06-F-01`, `PT06-F-02` |
| Denominators that moved between rounds | **`1`** — stock flows `17` → `18` |

---

## 2. Inventory convergence — Stock Truth

| Status | n | Members |
|---|---:|---|
| `RECONCILED` (incl. as a measured negative) | **`14`** | `IR-01`…`IR-14` |
| `PARTIAL` | **`3`** | `IR-15` asset capitalization from stock · `IR-16` cross-company transfer · `IR-17` consumption by a service or project |
| **`NOT RECONCILED`** | **`1`** | **`IR-18` Equipment / maintenance consumption** — *added by this register* |
| Total | **`18`** ✔ | |

**The denominator moved.** `SA06` measured **`17`** stock-affecting flows (`11 / 2 / 4`); CORR2 measures
**`18`** (`14 / 3 / 1`). **`IR-18` did not change status — it did not previously exist as a row.**

> **An improvement from `4 NOT RECONCILED` to `1` is real, and it is not the whole movement: the
> population grew by one at the same time, and the added row is the one that is unreconciled.** A round
> that both improves a ratio and enlarges its denominator must publish both, or the improvement reads
> larger than it is.

---

## 3. Accounting convergence — Financial Truth

| Status | n | Members |
|---|---:|---|
| `RECONCILED` (**incl. `5` `NO POSTING BY DESIGN`**) | **`15`** | `AR-01`…`AR-10`, `AR-13`…`AR-16`, `AR-28` |
| **`PARTIAL` — a named open element** | **`14`** | `AR-11`, `AR-12`, `AR-17`…`AR-27`, `AR-29` |
| `UNKNOWN` / `NOT RECONCILED` | **`0`** | — |
| Total | **`29`** ✔ | `AR-01`…`AR-29`, each exactly once; `15 + 14 + 0 = 29` |

**The `14` `PARTIAL` flows, named:** manufacturing consumption + FG receipt · scrap/variance · asset
derecognition · employee expense · time-based recognition · period/year close · analytic dimension
attribution · **tax determination and register** · sell-side commitment cancellation · dropship ·
kit/bundle · service completion · project · maintenance cost.

> **The claim `29 of 29 determined` is true and weaker than it sounds — the register says so itself:**
> *"That is a different and weaker claim than 'reconciled', and the distinction is the point."*
> **`15 of 29` are reconciled without an open element; `14` carry one.**

### 3.1 `PT06-F-01` — the register contradicts its own count table, and the error persists

| Statement | Location | Value |
|---|---|---:|
| count table, `PARTIAL` | `SA_CORR2_06` line 74 | **`14`** |
| **prose immediately beneath it** | line 90 | **`Thirteen`** |
| **its own checkpoint line** | line 206 | **`13`** |
| every downstream citation (`SA_CORR3_08`, `SA_CORR3_06`, `SC-30`, `SC-45`) | — | **`14`** |

**Enumerating the `PARTIAL` rows gives `14`.** The table and all downstream consumers are right; **the
register's own prose and checkpoint line are wrong, and were still wrong at the time of this reading.**

**A sibling defect exists in the inventory register** (`XMC-F-06`): `SA_CORR2_05` §2.1 publishes
`14 / 3 / 1` while **its own checkpoint line still reads `13 of 18 reconciled, 4 partial, 1 not
reconciled`.**

> **Both defects were found, published as `XMC-F-07` and `XMC-F-06`, and **neither checkpoint line was
> repaired**.** This is the recorded *a revision log is not a correction* pattern: the finding exists in a
> register, and the wrong text still stands in the artefact a reader would quote.

| | |
|---|---|
| Status | **OPEN — the defect is in the SOURCE text, not in this session's reading** |
| Effect on Pre-Test | **none on the numbers** — `PT-06` uses the enumerated `14 / 3 / 1` and `15 / 14 / 0` |
| Action | **`PT-15` must audit the artefact text by identifier, not the disposition column** |

---

## 4. Universal convergence — the rule, and where it is unsatisfiable

**`ND-09`, the governing determination:**

> *"A cross-module fulfilment that produces revenue **must** produce a cost recognition **bound to the same
> identity**, **or** an explicit, recorded determination that it does not."*

**And `XMC-C-C6` + `BD-ACC-01`:** cost binds to **the same canonical Accounting Event Identity** as
revenue, Tenant- and Company-bounded.

| Convergence obligation | State |
|---|---|
| Revenue → bound cost recognition, or a recorded determination | **specification complete; the binding identity is element 15 — not built** |
| Valuation basis | **`BD-ACC-03A`/`03B` — Product Category owns policy, values and method version** (`JT-01` **RULED**) |
| **Recognition timing** | **Boss election `JT-04`** — `ND-10` is the SMEs Core recommendation and is **NOT Boss-approved** |
| **Return / reversal cost basis** | **Boss election `JT-05`** — original vs current cost |
| Inter-company transfer treatment | **`JT-10` open** — joint Accounting × Inventory decision; the value leg is **untraced** |
| Dropship | cost binds to the same identity **or a recorded determination that none arises** (`XMC-C-C6`); `C2-D-02` **CLOSED**; remaining variable is **the date**, which is `F1`'s |
| Scrap | **no cost causality**; salvage object specified (`XMC-C-D7`); by-product valuation open |
| Manufacturing overhead | **fixed-overhead elements have no injection path** (`R-22 GAP`) |
| Manufacturing variance | **no variance mechanism exists** — one of nine recognised |

### 4.1 `PT06-F-02` — `ND-10` is a SMEs Core position carried as if it settled the timing question

**`ND-10`** defines *Perpetual* as recognition **at the physical movement** and *Periodic* as recognition
**at period close**, and requires both definitions to be stated wherever the terms appear.

**Its own status, verbatim:** *"**a SMEs Core position, carried as the recommendation on Boss election
`JT-04`, not Boss-approved**"*, and `SA_CORR2_12` records that *"none is Boss-approved"*.

**Two hazards, both already realised once in the corpus:**

1. **A prior round read *Perpetual* as *"recognition on the physical event date"* by construction** and was
   falsified by its own self-challenge (`CHC-01`, `C10-A1` **withdrawn**) — *"It was SMEs Core deciding an
   item the owning package reserved to Boss."* **The reference generation's own label reads
   *"Perpetual (at invoicing)"*** — i.e. the vendor word means something different, and taking it would
   invert the answer.
2. **The attribution of `ND-10`'s Boss item differs between two current artefacts:**

| Artefact | `ND-10` routed to |
|---|---|
| `SA17` **CORR5 controlled** | **`JT-04`** |
| `SA17` **`FINAL_CONTROLLED_V2`** | **`F1`** |

**Both are current-generation files; both are reported; neither is reconciled here.** (`F1` is the Boss
*family* containing `JT-04`/`JT-05`, so these are plausibly the same item at two granularities — **but
that reconciliation is not stated in either file, and a denominator built on "F1" is not the same as one
built on "JT-04".**)

| | |
|---|---|
| Status | **OPEN — carried, not resolved** |
| Binding | **`PT-12` states `ND-10` as a *recommendation*, never as a determination**, and names `JT-04` **and** `F1` until an authority reconciles them |
| Routed to | `PT-11` (authority register), `PT-13`, **B-7** |

---

## 5. Per-scenario convergence obligation — the `22`

**Both consequences are tested on every scenario; `N/A` requires a reason.**

| Convergence dimension | `C` | `B` | `G` |
|---|---:|---:|---:|
| **`IC`** Inventory convergence | **`22`** | `0` | **`0`** |
| **`AC`** Accounting convergence | **`12`** | **`10`** | **`0`** |

**The `10` `AC` `B` cells are scenarios `1,2,3,4,5,6,8,9,16,17`** — Boss election `JT-04`, with `8`/`9`
additionally `JT-05`. **These are exactly the `11 of 22` el.`4`/`7` rows less `X-19`**, which carries the
period-object dependency rather than a Boss election.

**`S` markers — Thai statutory holds inside `AC` cells: `9`** (rows `1,2,3,4,5,6,9,13,19`). **An `S` is a
statutory evidence hold, not a Phase SA gap** — and it is **not** the same unit as the `4` Thai statutory
items in the external-dependency register. **`9` markers ≠ `4` items.**

> **`0` `G` cells in either convergence dimension.** Every convergence gap across the `22` is a **Boss
> election** or a **statutory hold** — none is a SMEs Core specification gap. **This is the finding that
> `PT03-F-01` requires be stated with its ownership qualifier attached, and it is so stated here.**

---

## 6. `NO POSTING BY DESIGN` — the convergence result that is easiest to misread

**`5` of the `15` accounting-`RECONCILED` flows are reconciled *because they post nothing*.**

**`AR-10` internal transfer (same company) is the exemplar:** `RECONCILED — NO POSTING BY DESIGN`, and its
control is `SA06-F-05` — **neutrality *asserted*, not configured** — with `R4-F-18` recording that **no
independent check exists** and that **one configuration change breaks two flows**.

> **A flow that reconciles by posting nothing is reconciled only for as long as the nothing holds.**
> `PT-12` carries these `5` with an explicit negative test: **the expected result is the absence of a
> posting, and the test must be able to detect a posting that should not be there** — otherwise it is a
> test that returns clean and means nothing (`SA17` §2b prohibition 2, applied here by analogy).

---

## 7. Checkpoint

> ## `CP-PT-06 — ACCOUNTING/INVENTORY CONVERGENCE MAPPED, NOT PROVEN`
>
> **Stock Truth `14 / 3 / 1` of `18`, with the denominator's move from `17` published beside the
> improvement — **the one unreconciled flow (`IR-18` equipment/maintenance consumption) is the row the
> round added** · Financial Truth `15 / 14 / 0` of `29`, of which **`5` reconcile by posting nothing** ·
> `0 of 29` flows lack an accounting semantic, and **`14 of 29` carry a named open element** ·
> `IC` `22 C`, `AC` `12 C / 10 B`, **`0 G` in both** — every convergence gap is a Boss election or a
> statutory hold, **stated with its ownership qualifier as `PT03-F-01` requires** ·
> **`PT06-F-01`: two registers each contradict their own checkpoint line (`13` vs `14`; `13/4/1` vs
> `14/3/1`), both already published as findings, **neither repaired** — `PT-15` must audit the text** ·
> **`PT06-F-02`: `ND-10` is a SMEs Core recommendation, NOT Boss-approved; one prior round already
> decided it in Boss's place and withdrew; its Boss item is attributed to `JT-04` in one current artefact
> and `F1` in another.**
>
> **`0` convergence results improved · `0` Boss elections answered · `0 of 22` verified.**

Next checkpoint: `PT-07 — Manufacturing / Purchase / Dropship Challenge`.

No Evidence = No Progress. Never Skip Gate. Truth over Pass. A specification is not a control.
Boss remains the sole Final Approver.
