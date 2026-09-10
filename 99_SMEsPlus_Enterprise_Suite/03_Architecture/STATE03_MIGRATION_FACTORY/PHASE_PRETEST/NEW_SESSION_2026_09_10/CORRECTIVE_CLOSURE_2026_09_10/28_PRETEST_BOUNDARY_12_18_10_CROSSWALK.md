# 28 — BOUNDARY CROSSWALK `12 ↔ 18 ↔ 10`

## `CHECKPOINT C (part 2) — CORE-04 EXECUTED · 4 BOUNDARIES OUTSIDE THE DECLARED DENOMINATOR`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7-RETURN-CORR1-001]` · Boss: **SOLE FINAL APPROVER**

> **`B4′` declared a `12`-class denominator on NEW Boss authority. This file does NOT expand, rewrite or
> reinterpret it. It maps it, and where the map does not close it prepares a Boss item.**

---

## 1. The three populations, each from its own primary source

| Set | n | Source | Unit |
|---|---:|---|---|
| **α — declared boundary classes** | **`12`** | **`22_` §1**, on `B4′` (NEW Boss authority, not inherited from `PT11-P-01`) | boundary **class** |
| **β — tested handoff rows** | **`18`** | `SA_CORR3_08` §6, *"`XMC-H-01`…`XMC-H-18`, each exactly once"* — tally `0 PROVEN / 2 N/A / 16 HOLD — EXACT GAP` = `18` ✔ | handoff **row** |
| **γ — contract-proof flows** | **`10`** | `SA_CORR4_02` §5 — tally `2 CONTRACT-SUFFICIENT / 8 CONTRACT-GAP` = `10` ✔ | **flow** |

**Three different units. `CC-F-02`'s warning is preserved: they are not interchangeable.**

---

## 2. The crosswalk — executed

| α class | β row(s) | γ flow(s) | β disposition | Mapped? |
|---:|---|---|---|:--:|
| `1` Sales → Inventory | `XMC-H-01` | `1` | `HOLD — EXACT GAP` | ✔ |
| `2` Sales → Manufacturing | `XMC-H-02` | `2` | `HOLD — EXACT GAP` | ✔ |
| `3` Sales → Purchase (dropship/buy/MTO) | `XMC-H-03` | `3` | `HOLD — EXACT GAP` | ✔ |
| `4` Manufacturing → Inventory | `XMC-H-04` | `6` (first leg) | `HOLD — EXACT GAP` | ✔ |
| `5` Inventory → Accounting | `XMC-H-05` | `5`, `6` (2nd leg) | `HOLD — EXACT GAP` | ✔ |
| `6` Sales → AR / Accounting | `XMC-H-06` | `7` (collapsed) | `HOLD — EXACT GAP` | ✔ |
| `7` Purchase → AP / Accounting | `XMC-H-07` | `7` (collapsed) | `HOLD — EXACT GAP` | ✔ |
| `8` Payment → Bank / Accounting | `XMC-H-08` | `7` (collapsed) | `HOLD — EXACT GAP` | ✔ |
| `9` Asset → Accounting | `XMC-H-09` | `8` | `HOLD — EXACT GAP` | ✔ |
| `10` Expense → Accounting | `XMC-H-10` | `9` | `HOLD — EXACT GAP` | ✔ |
| `11` Tax → Accounting / reporting | `XMC-H-11` | `10` | `HOLD — EXACT GAP` | ✔ |
| `12` Close → required subledgers | `XMC-H-12` | **— none —** | `HOLD — EXACT GAP` | ✔ (β only) |

**α maps `1:1` and in order onto `XMC-H-01…12`. The correspondence is exact, which is itself evidence
that the declared `12` was derived from the first twelve rows of the `18`.**

### 2.1 Rows of β that map to NO declared class

| β row | Handoff | β disposition | γ? | Class |
|---|---|---|:--:|---|
| **`XMC-H-13`** | **Inventory → Sales and Purchase** | `HOLD — EXACT GAP` | no | **`C`** |
| **`XMC-H-14`** | **Quality → Inventory** | `HOLD — EXACT GAP` | no | **`C`** |
| `XMC-H-15` | Quality hold → Accounting | `NOT APPLICABLE — EVIDENCE-BACKED` | no | **`B`** |
| `XMC-H-16` | Internal transfer → Accounting | `NOT APPLICABLE — EVIDENCE-BACKED` | no | **`B`** |
| **`XMC-H-17`** | **Service / Project performance → Accounting** | `HOLD — EXACT GAP` | no | **`C`** |
| **`XMC-H-18`** | **Migration / replay → Inventory and Accounting** | `HOLD — EXACT GAP` | no | **`C`** |

### 2.2 Members of γ that map to no α class

| γ flow | Status |
|---|---|
| **`4` Purchase → Inventory** | **In γ, absent from α and absent from β.** `CORR4` added it; neither the declared `12` nor the tested `18` carries it. **A third inconsistency, and it runs the opposite way from §2.1** |

**γ additionally *collapses* α classes `6`/`7`/`8` into one row and *drops* α class `12` entirely.**

---

## 3. `H-13` / `H-14` / `H-17` / `H-18` — classified `A` / `B` / `C` / `D`, one each

**Test applied to each: (i) is it a subcase of a declared class — same producer, same consumer, same fact
class? (ii) does it carry a business fact across a module boundary, or is it an attribute of another
flow? (iii) is the evidence sufficient to decide?**

| Row | (i) subcase of a declared class? | (ii) crosses a module boundary with a business fact? | (iii) evidence sufficient? | **CLASS** |
|---|---|---|---|---|
| **`XMC-H-13`** Inventory → Sales and Purchase | **NO.** α`1` and α`3` are Sales→Inventory and Sales→Purchase — **opposite direction, different producer, different fact class** (availability/progress/transfer status, not demand) | **YES.** `SA_CORR3_08`: sell-side header progress and transfer status are *"independently re-derived rather than read"*, and *"two derivations of one fact can disagree after a partial cancellation, a return or a correction, and **nothing reconciles them**"* — a cross-module fact with no published contract | YES | **`C` — genuine additional material boundary** |
| **`XMC-H-14`** Quality → Inventory | **NO.** No Quality producer appears in α at all | **YES.** *"The route is **Boss-ruled verbatim** and the accounting answer is determinate."* The gap is the **object**, not the boundary — *"the Quality object itself is absent — `0` blobs, two shapes, firing positive controls"* | YES — the boundary is evidenced and Boss-ruled; only its object is absent, which is a **content** gap, not an **existence** gap | **`C` — genuine additional material boundary** |
| **`XMC-H-17`** Service / Project performance → Accounting | **NO.** Not α`5` (no stock moves); not α`10` (this is performance recognition, not expense) | **YES**, and it carries **accounting facts**. *"`BD-ACC-01` presumes a business fact owned by a source module; for a service there is **no physical fact, only an assertion, with no event record**"*; the project derivation *"writes three costed rows from one duration, with two report surfaces reading different row sets"* | YES | **`C` — genuine additional material boundary** |
| **`XMC-H-18`** Migration / replay → Inventory **and** Accounting | **NO.** Migration is a distinct producer; **dual-target**, which no declared class is | **YES.** `HX-24` is *"the only **dual-target** handoff"*, carrying *"certified opening balances, **quantity and value**"*. **`B9′` has already admitted `MF-01` → `IR` and `AR` and `MF-02` → `IR` — flows that travel on exactly this boundary** | YES | **`C` — genuine additional material boundary** |
| `XMC-H-15` / `XMC-H-16` | n/a | **NO** — internal→internal, emits no valuation fact; `N/A` with reason, *"which the approval expressly permits"* | YES | **`B` — non-boundary for the element-contract denominator.** Not proposed for admission. **Caveat preserved:** `SA_CORR3_08` §2.6 records that the `N/A` is evidence-backed **and its protection is not** — a configuration change could make `H-16` emit |

**Result: `4 × C` · `2 × B` · `0 × A` · `0 × D`.**

### 3.1 Why `A` was tested and rejected rather than assumed

**`A` was the outcome that would have closed this item without a Boss act, and it was tested first.**
For each of the four, a subcase reading was constructed and failed on a *named* attribute — direction
(`H-13`), producer absent from α (`H-14`), fact class (`H-17`), target cardinality (`H-18`).
**Declining the cheap answer is recorded because it is the half that costs something.**

---

## 4. `BOSS-CORR1-01` — boundary denominator correction item

> ### The declared `12` does not cover the tested population, and SMEs Core may not enlarge it.

| | |
|---|---|
| **Item** | **`BOSS-CORR1-01`** |
| **Authority required** | **Boss** — `B4′` was a *"NEW Boss authority declaration"*; only its issuer may amend its membership. `SC-04` §1's rule applies by analogy: SMEs Core *"may **NOT**… enlarge its population"* |
| **The exact question** | Do `XMC-H-13`, `-14`, `-17` and `-18` join the declared boundary denominator, or is each given a **declared exclusion with a reason**? |
| **Why it cannot be resolved below Boss** | Every non-Boss route was attempted (§3): three are not subcases on named attributes, two are evidence-backed `N/A`, and none is an evidence question — the evidence is complete and consistent. **What is missing is an authority act, not a fact** |
| **Consequence if `12` stands unamended** | `SC-BD-02` §7 fixes **the Pre-Test Matrix element-contract denominator** at these `12`. Four handoffs carrying `HOLD — EXACT GAP` are then **outside the contracted and tested surface** — including `XMC-H-18`, onto which `B9′` has already admitted two flows. **A denominator and an admission ruling would be pointing at different populations** (`B7-F-08`) |
| **Consequence if `12 → 16`** | element-contract applicability, `HF-CTX-06`/`-11` attestation and Pre-Test Matrix scope extend to `16`; `CORE-04`'s mapping is then closed by this file plus the amendment |
| **Options for Boss** | **(a)** admit all four → `16` · **(b)** admit a named subset · **(c)** declare exclusions with reasons, leaving `12` · **(d)** rule the denominator is `18` (β) and retire α |
| **SMEs Core recommendation** | **(a)** — with `XMC-H-18` the least deferrable, because a ruling has already admitted flows onto it. **Stated as a recommendation, not applied** |
| **What this round did NOT do** | **`0` boundaries added. `0` classes rewritten. The declared `12` stands unamended in every register until Boss acts** |

---

## 5. `CORE-04` — status

| | |
|---|---|
| Mapping `α ↔ β` | **DERIVED** — §2, `12` exact, `6` unmapped |
| Mapping `α ↔ γ` | **DERIVED** — §2, with `γ`'s own three deviations named at §2.2 |
| Mapping to migration additions | **DERIVED** — `MF-01`/`MF-02` travel on `XMC-H-18`, unmapped |
| **`CORE-04`** | **DISCHARGED as a mapping obligation.** The mapping is executed and published. **What remains is not a mapping act but `BOSS-CORR1-01`** |
| Per-boundary applicability declaration (`SC-11` §6 obl. `5`) | **STILL BLOCKED** — it cannot be written against a population Boss may be about to change. **Blocked on `BOSS-CORR1-01`, no longer on "no set exists"** |

---

## 6. Checkpoint

> ## `CHECKPOINT C (part 2) — CORE-04 EXECUTED`
>
> **`α 12 ↔ β 18 ↔ γ 10` mapped at named-member level · **α maps `1:1` and in order onto `XMC-H-01…12`** ·
> **`6` β rows outside α: `4` classified `C` (genuine additional material boundaries), `2` classified `B`** ·
> `γ` deviates in three further ways — **adds `Purchase → Inventory`, collapses α`6`/`7`/`8`, drops α`12`** ·
> **`A` (subcase) tested first and rejected on a named attribute in every case** ·
> **`BOSS-CORR1-01` prepared; `0` boundaries added by SMEs Core; the declared `12` stands unamended** ·
> `CORE-04` discharged as a mapping obligation.**

No Evidence = No Progress. No count without named membership. Boss is the sole Final Approver.
