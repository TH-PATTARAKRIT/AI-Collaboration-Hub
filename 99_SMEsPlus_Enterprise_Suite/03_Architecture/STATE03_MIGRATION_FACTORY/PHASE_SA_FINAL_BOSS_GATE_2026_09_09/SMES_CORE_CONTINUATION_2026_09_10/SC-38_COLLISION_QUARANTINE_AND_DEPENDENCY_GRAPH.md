# SC-38 — COLLISION QUARANTINE AND DEPENDENCY GRAPH

## CP-SA-SC-290 — COLLISION QUARANTINED WITHOUT DATA LOSS

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · head consumed `e2e3f3dc`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **PROCEDURAL QUARANTINE ONLY.** Nothing is deleted, rewritten, invalidated or ranked. **`0` bytes of
> either record changed** — verified.

---

## 1. The quarantine, stated exactly

Both records are marked:

> ## `COLLISION-TAINTED AUTHORITY RECORD — PRESERVED FOR LINEAGE — NOT SAFE AS A PROSPECTIVE TIEBREAKER UNTIL CANONICAL BOSS RE-RULING`

| Record | Ruling | Content status | Prospective use |
|---|---|---|---|
| **`SC-BD-01`** | `FG-F-06 = READING B` | **INTACT — byte-identical, not modified** | **QUARANTINED** as a tiebreaker |
| **`SC-CONTRA-01`** | `FG-F-06 = READING A` | **INTACT — byte-identical, not modified** | **QUARANTINED** as a tiebreaker |

**What quarantine means here, and what it does not:**

| Quarantine DOES | Quarantine does NOT |
|---|---|
| stop either record being used **prospectively** to settle the gate question | erase, rewrite or invalidate either record |
| record that both were issued in **mutual blindness** and so cannot function as corrections of each other | say either ruling was wrong |
| require a **fresh canonical ruling** before the gate question is settled | rank them, or prefer one |
| preserve both as **historical lineage after** that ruling | remove either from the manifest or the evidence index |

**The taint is procedural — it attaches to the *collision*, not to either reading's merits.** The
substantive merits are re-derived independently from primary text at `SC-39`, **without inheriting either
record's conclusion**.

---

## 2. The 16 downstream rulings — classified, not judged

**Every one is classified exactly as `06_` §3 requires:**

> ## `SUBSTANTIVE BOSS RULING EXISTS / GATE-PRECONDITION STATUS PENDING CANONICAL REVALIDATION`

| Record | Family | Atomic IDs ruled | Substantive ruling | Gate precondition |
|---|---|---|---|---|
| `SC-BD-02` | `F4` | `XMC-D-02`, `C2-D-01` | **EXISTS** | **PENDING** |
| `SC-BD-03` | `F6` | `MTI-D-04`, `TV6-BOSS-02` | **EXISTS** | **PENDING** |
| `SC-BD-04` | `F7` | `RC-D-01`, `RC-D-02`, `CF-D-01`, `CF-D-02` | **EXISTS** | **PENDING** |
| `SC-BD-05` | `F1` | `JT-04`, `JT-05` | **EXISTS** | **PENDING** |
| `SC-BD-06` | `F5` | `POH-D-06` | **EXISTS** | **PENDING** |
| `SC-BD-07` | `F2` | `XD1-P1`, `TV6-BOSS-01`, tolerance default | **EXISTS** | **PENDING** |
| `SC-BD-08` | `F3` | `XMC-D-01`, `C2-D-02` | **EXISTS** | **PENDING** |
| `SC-BD-09` | `F8` | `C-02` | **EXISTS** | **PENDING** |
| `SC-BD-10` | acts | 4 of 5 acts approved | **EXISTS** | **PENDING** |

**`16` atomic decisions across `SC-BD-02`…`SC-BD-09`, plus the acts ruling.**

> **NOT presumed void. NOT presumed safe. NOT re-asked.** `06_` §3: *"Do NOT re-ask all 16 unless the new
> canonical ruling actually changes their validity."* **§4 below establishes, per ruling, whether it could.**

---

## 3. The dependency graph

```
FG-F-06 AUTHORITY BASIS            [ COLLIDED — no canonical basis exists ]
        |
        v
GATE ADMISSIBILITY                 [ was the F1–F8 gate open when the 16 were ruled? ]
        |                            Reading A -> NO.  Reading B -> YES.
        v
DEPENDENT RULINGS                  [ 16 substantive rulings, precondition PENDING ]
        |
        +--> SCENARIO CONSEQUENCES [ 0 rows move — SC-45 §3, re-proven ]
        |
        +--> VETO CONSEQUENCES     [ 0 vetoes move — §5 ]
        |
        v
PRE-TEST ENTRY                     [ blocked on the canonical ruling, not on any SMEs Core work ]
```

### 3.1 The graph's load-bearing property

> **The dependency runs one way and stops.** `FG-F-06` determines **admissibility**, and admissibility
> attaches to **the act of ruling**, not to **what was ruled**. **No scenario row, no veto, no invariant
> and no contract changes on either branch** — proven at §4 and §5, re-proven at `SC-45`.
>
> **Consequence: the blast radius is exactly 16 rulings' preconditions and nothing else.** That is a much
> smaller exposure than "16 rulings may be void", and it is the difference between a re-ruling and a
> re-derivation.

---

## 4. Per-ruling revalidation test — could the canonical ruling change its validity?

**Test applied: does this ruling's *substance* depend on which reading is canonical?**

| Ruling | Substance depends on `FG-F-06`? | Why |
|---|---|---|
| `SC-BD-02` `F4` | **NO** | Contract scope and binding strength are architecture elections; `8C-001` says nothing about either |
| `SC-BD-03` `F6` | **NO** | Cross-company grant policy rests on `BD-ACC-02` and `MTI-*`, not on the exit constitution |
| `SC-BD-04` `F7` | **NO** | Authorization axes rest on `MTI-D-02`/`-D-03` |
| `SC-BD-05` `F1` | **NO** | COGS recognition rests on `BD-ACC-01`/`03A`/`03B` and `08_JT04`/`09_JT05` |
| `SC-BD-06` `F5` | **NO** | The restatement rests on `SA_CORR3_03`; its completion depends on **AAS+**, not on `FG-F-06` |
| `SC-BD-07` `F2` | **NO** | A risk-appetite election |
| `SC-BD-08` `F3` | **NO** | Rests on `XMC-F-03` + `BD-ACC-03A` |
| `SC-BD-09` `F8` | **NO** | Severity election; the object is ruled by `BD-ACC-01` |
| `SC-BD-10` acts | **NO** | Commissioning acts |

> **`0` of the 16 have substance that depends on `FG-F-06`.** **What depends on it is whether the gate was
> open when they were made** — a procedural property of the ruling act.
>
> **Therefore, on either canonical outcome, the correct remedy is at most re-affirmation, never
> re-derivation.** If Boss's canonical ruling makes the gate retrospectively closed, the substance survives
> and only the act needs re-issuing. **SMEs Core does not decide that; it establishes that the question is
> narrow.**

---

## 5. Veto consequences — none

**`6` in force · `0` discharged · `0` self-discharged.** No veto's trigger references `FG-F-06`, the
constitution's exit criteria, or the gate's openness. **`RC-V-01` bars implementation start on every
branch, from AAS+/RC authority, independent of `8C-001`.** `AAS-V-03` and `CF-V-02` turn on `MTI-D-04`
(ruled at `SC-BD-03`, precondition pending) — **so their status inherits the same pending flag and nothing
more.**

---

## 6. Data-loss check

| Check | Result |
|---|---|
| `SC-BD-01` byte-identical | **YES** |
| `SC-CONTRA-01` byte-identical | **YES** |
| `SC-BD-02`…`SC-BD-10` byte-identical | **YES — all 9** |
| `SC-11`, `SC-12`, `SC-13`…`SC-21` byte-identical | **YES — all 11** |
| Records deleted, rewritten or removed from the manifest | **`0`** |
| Force-pushes | **`0`** |

---

## 7. Checkpoint

> ## `CP-SA-SC-290 — COLLISION QUARANTINED WITHOUT DATA LOSS`
> **Both authority records quarantined **procedurally**, both **byte-identical** · 16 rulings classified
> *substantive exists / precondition pending* — **`0` presumed void, `0` presumed safe, `0` re-asked** ·
> dependency graph published, and it **terminates**: `0` scenario rows, `0` vetoes, `0` invariants move ·
> **`0` of 16 have substance depending on `FG-F-06`**, so the maximum remedy is re-affirmation ·
> **`0` records lost, `0` force-pushes.**

No Evidence = No Progress. Never Skip Gate. Quarantine preserves; it does not judge.
Boss remains the sole Final Approver.
