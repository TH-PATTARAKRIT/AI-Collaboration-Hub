# 05 — BOUNDARY `12 ↔ 18 ↔ 10` RECONCILIATION

## `CHECKPOINT D (part 2) — CORE-04 EXECUTED · 4 GAP-CARRYING HANDOFFS OUTSIDE THE DECLARED SET`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-RECOVERY-NEWSESSION-001]` · Boss: **SOLE FINAL APPROVER**

> **§6C: *"Do not silently expand the Boss-declared denominator."* — The declared `12` is NOT expanded.**

---

## 1. `12 ↔ 18` — the crosswalk, verified at primary text

| `XMC-H` | Handoff | Declared class | `SA_CORR3_08` disposition |
|---|---|---|---|
| `-01` | Sales → Inventory | **1** | `HOLD — EXACT GAP` |
| `-02` | Sales → Manufacturing | **2** | `HOLD — EXACT GAP` |
| `-03` | Sales → Purchase (dropship/MTO) | **3** | `HOLD — EXACT GAP` |
| `-04` | Manufacturing → Inventory | **4** | `HOLD — EXACT GAP` |
| `-05` | Inventory → Accounting | **5** | `HOLD — EXACT GAP` |
| `-06` | Sales → AR/Accounting | **6** | `HOLD — EXACT GAP` |
| `-07` | Purchase → AP/Accounting | **7** | `HOLD — EXACT GAP` |
| `-08` | Payment → Bank/Accounting | **8** | `HOLD — EXACT GAP` |
| `-09` | Asset → Accounting | **9** | `HOLD — EXACT GAP` · **missing consumer** |
| `-10` | Expense → Accounting | **10** | `HOLD — EXACT GAP` |
| `-11` | Tax → Accounting/reporting | **11** | `HOLD — EXACT GAP` |
| `-12` | Close → all subledgers | **12** | `HOLD — EXACT GAP` |
| **`-13`** | **Inventory → Sales and Purchase** | **— NONE —** | `HOLD — EXACT GAP` · *"MATCH, with a **named hazard**"* — progress and transfer status **independently re-derived**, two derivations of one truth |
| **`-14`** | **Quality → Inventory** | **— NONE —** | `HOLD — EXACT GAP` · *"MATCH on routing; **GAP on the object**"* — **the Quality object itself is absent** |
| `-15` | Quality hold → Accounting | — none — | **`NOT APPLICABLE — EVIDENCE-BACKED`** — internal→internal emits no valuation fact |
| `-16` | Internal transfer → Accounting | — none — | **`NOT APPLICABLE — EVIDENCE-BACKED`** |
| **`-17`** | **Service / Project performance → Accounting** | **— NONE —** | `HOLD — EXACT GAP` · *"`BD-ACC-01` presumes a business fact owned by a source module; **for a service there is no physical fact, only an assertion**"* |
| **`-18`** | **Migration / replay → Inventory and Accounting** | **— NONE —** | `HOLD — EXACT GAP` · *"**the provenance reference does not exist** (element 14); replay requires a stable identity (element 15)"* |

**Mapped: `12` · Unmapped: `6` · Of the unmapped, `NOT APPLICABLE — EVIDENCE-BACKED`: `2` ·
**gap-carrying and outside the contracted surface: `4`** — `-13`, `-14`, `-17`, `-18`.**

**Tally check:** `12 + 2 + 4 = 18` ✔ · `SA_CORR3_08`'s own disposition `0 PROVEN / 2 N/A / 16 HOLD = 18` ✔.

---

## 2. `B7-F-07` — the coverage hole, stated exactly

`SC-BD-02` §7 fixes **the Pre-Test Matrix element-contract denominator** at the declared boundaries.
**`B4′` declared `12`, and they are `XMC-H-01…12` exactly.**

> **`4` handoffs that the tested register records as carrying an exact gap are therefore OUTSIDE the
> contracted and tested surface.** The declaration closed the denominator question and left a **measured**
> coverage hole the package had never measured.

**What is NOT claimed:** that the declared `12` is the wrong set. **Declaring it is a Boss authority act
and is not falsifiable here.** Only its **coverage against the tested population** was measured.

---

## 3. `B7-F-08` — two rulings in tension

| | |
|---|---|
| **`B9′`** | **ADMITS** `MF-01`/`MF-02` into `IR` (`18→20`) and `AR` (`29→30`) |
| **`B4′`** | **EXCLUDES** `XMC-H-18` — *migration/replay → Inventory and Accounting* — from the contracted `12` |
| **The tension** | **the admitted flows travel on the excluded handoff**, and `XMC-H-18` is the row recorded as *"elements `14` and `15` `NOT SUPPLIABLE`"* |

**Neither ruling is wrong. They were applied in the same register and never put against each other.**

**Consequence:** the migration flows are **inside** the flow-convergence population and **outside** the
element-contract surface. **A flow whose handoff carries no element contract cannot have its handoff
elements tested** — so admitting it closes an enumeration gap and opens an untestable one.

**Recorded as an unresolved material contradiction. Exit condition `16` therefore remains `FAIL`.**

---

## 4. `12 ↔ 10` — **NOT DERIVED**

`SA_CORR4_02` §5's **`10`** contract rows are a **third granularity** (`2 CONTRACT-SUFFICIENT` ·
`8 CONTRACT-GAP`).

| | |
|---|---|
| Derived here? | **NO** |
| Derived by B-7? | **NO** — its §5 item `6` names this as a limitation of its own review |
| Status | **`CORE-04` PARTIALLY EXECUTED — the `12 ↔ 18` leg is done; the `12 ↔ 10` leg is not** |
| Why not closed | the `10` rows are **flow-shaped**, not boundary-shaped (they collapse AR/AP/Payment/Bank into one and add `Purchase → Inventory`). **Mapping them requires a determination about which granularity governs — a scope act, not a transcription** |

> **Two independent parties have now left the same leg underived. Recording it as owed rather than
> asserting a mapping.**

---

## 5. Checkpoint

> ## `CHECKPOINT D (part 2) — `12 ↔ 18` EXECUTED`
>
> **`12` mapped · `2` `NOT APPLICABLE — EVIDENCE-BACKED` · **`4` gap-carrying handoffs outside the
> declared set** (`-13`, `-14`, `-17`, `-18`); `12+2+4 = 18` ✔ · the declared `12` is **NOT expanded** ·
> **`B7-F-08` confirmed — `B9′` admits flows onto the handoff `B4′` excludes**, an unresolved material
> contradiction · **`12 ↔ 10` remains UNDERIVED by both parties and is recorded as owed.**

