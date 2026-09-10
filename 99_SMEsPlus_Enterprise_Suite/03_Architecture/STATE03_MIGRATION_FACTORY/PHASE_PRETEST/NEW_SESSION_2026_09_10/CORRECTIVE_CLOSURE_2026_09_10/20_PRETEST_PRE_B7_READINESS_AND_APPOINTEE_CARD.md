# 20 — PRE-B7 READINESS AND APPOINTEE CARD

## `B-7 NOT EXECUTED · APPOINTEE CARD PREPARED · RE-FREEZE PENDING BOSS RULING`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-BOSS-RESOLUTION-001]` · Boss: **SOLE FINAL APPROVER**

> **§12: *"DO NOT execute B-7 in this session."* — obeyed. `0` execution, `0` simulation, `0` delegation.**

---

## 1. Baseline status — why `172d7b9c` is NOT the B-7 baseline

| | |
|---|---|
| Pre-ruling frozen baseline | **`172d7b9c`** — deliverables `01_`…`13_` |
| Superseded by | this round's `17_`…`21_`, **and** the `CORE-01` correction which **changes the Boss decision set** (`B1` `4 → 6`) |
| **Consequence** | **`172d7b9c` is Audit Lineage, not the challenge baseline.** A challenger routed at it would attack a decision set that no longer exists |
| **The real B-7 baseline** | **created at `CHECKPOINT I`, after Boss rulings are applied** — `23_`/`24_` |
| Overwritten? | **`0`** — `172d7b9c` remains addressable and unmodified |

---

## 2. Eligibility criteria — testable, not aspirational

| # | Criterion | How a candidate is TESTED against it |
|---:|---|---|
| 1 | **Did not author `01_`…`21_` or `PT-00`…`PT-17`** | commit authorship on the canonical branch; session identity |
| 2 | **Did not author the corrective conclusions** | did not produce `CC-F-01`…`CC-F-12` |
| 3 | **Receives the frozen evidence read-only** | **cannot push to the canonical branch** — enforced by `PT-17`'s single-writer ruling |
| 4 | **Cannot modify challenged evidence before verdict** | publishes to **its own** evidence channel |
| 5 | **Attacks primary evidence independently** | must re-derive from `SC-*`/`SA_*` primaries, **not** from `01_`…`21_` conclusions |
| 6 | **No incentive or mandate to obtain a pass** | mandate says **FALSIFY**; a clean return is a permitted outcome only with a falsification attempt recorded per target |
| 7 | **Can issue `PASS` / `FAIL` / `HOLD` independently** | executor **cannot** convert `HOLD`/`FAIL` to `PASS` — §17 of the parent prompt |
| 8 | **Complete audit trail** | commands + outputs published, not patterns |
| 9 | **Explicitly appointed by Boss** | named in a Boss record |

### 2.1 Routes assessed

| Route | Eligible? | Ground |
|---|---|---|
| This executor | **NO** | authored everything; `SC-51` §4 *"NOT ELIGIBLE"* |
| A same-session subagent | **NO** | `SC-51` §4 *"same-session subagents are not independent"* |
| **A NEW session of the same model family, no shared context, read-only branch access** | **CONDITIONALLY YES** | fails criterion 1 only if it inherits this session's context. **With a fresh session and no transcript inheritance it satisfies 1–8; criterion 9 is Boss's act.** `SC-51` §4 warns only that a different **branch** does not by itself confer independence — it does not bar a fresh session |
| A different model / different vendor, fresh session | **YES — STRONGEST** | satisfies 1–8 with the widest margin on criterion 5 (no shared priors with the author) |
| The prior peer track | **NO — not automatically** | `SC-51` §4 |

### 2.2 Recommendation

> **STRONGEST ROUTE: a different model or vendor, in a NEW session, with read-only access to the frozen
> commit and NO inheritance of this session's transcript.**
>
> **ACCEPTABLE ROUTE: a new session of the same model family under the same constraints** — weaker on
> criterion 5, because shared training priors can reproduce the author's blind spots. **This programme has
> already measured that risk: three findings in this package were superseded-source citations of the same
> defect class, made repeatedly by the same executor.**

**SMEs Core names `0` candidates.** Naming one would breach criterion 9 and compromise 6.

---

## 3. What the challenger receives

| | |
|---|---|
| Frozen commit | **`23_`/`24_`, post-ruling** — not `172d7b9c` |
| Corrections that MUST travel | `PT00-F-01` scope **`64` → `76`** · register names (`SA15`/`SA17` `FINAL_CONTROLLED_V2`) · `a1fc7cd6` is a **blob** · `185+13+9≠198` is **not** an overcount · §5's **two different `12`s** |
| **New correction this round** | **`CORE-01` was discharged at `SC-14`/`SC-15`; `PT-11`/`13_`/`16_` were wrong to carry it open** |
| Attack order | **#1 the `19/2/1` split** · #2 `CLASS C` veto count · #3 the `B4′` declared set · #4 every Boss ruling implementation · #5 the `48` denominator · #6 migration admission · #7 **deference** · #8 the `E2E-04` re-grade refusal |

---

## 4. Pre-B7 readiness

| Condition | State |
|---|---|
| Corrective package published | **YES** — `01_`…`21_` |
| SMEs Core obligations closed | **YES — `0` open** (`17_`) |
| Boss decisions decision-ready | **YES — `9` cards** (`18_`) |
| External dependencies reconciled | **YES — `13`** (`19_`) |
| **Boss rulings applied** | **NO — pending** |
| **Post-ruling re-freeze** | **NO — `CHECKPOINT I`** |
| **Appointee named** | **NO — `B7′`** |
| **B-7 executable** | **NO** |

---

## 5. Checkpoint

> **`172d7b9c` demoted to Audit Lineage — the `CORE-01` correction changed the decision set, so a
> challenger routed there would attack a set that no longer exists · `9` testable eligibility criteria ·
> strongest route recommended (**different model/vendor, fresh session, read-only**), acceptable route
> named with its measured weakness · **`0` candidates named by SMEs Core** · **B-7 NOT EXECUTED.**

