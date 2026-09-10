# 10 — `E2E-04` TRAVERSABILITY PROOF

## `E2E-04 REMAINS HOLD — THE RE-GRADE IS NOT THIS SESSION'S TO MAKE`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-CORRECTIVE-CLOSURE-001]` · Boss: **SOLE FINAL APPROVER**

> **§13: *"If any mandatory node cannot be traversed: `E2E-04` remains `HOLD`."***

---

## 1. The chain, node by node

**Route: Sales → Manufacture → RM shortage → Purchase → Receipt → Production → Delivery.**

| # | Node | State | Evidence |
|---:|---|---|---|
| 1 | **Trigger** — sales order for a manufactured item | **TRAVERSABLE** | `BN-04` `PARTIAL` (`SA_CORR2_02` §3.1) |
| 2 | **Business action** — make-or-buy resolution | **TRAVERSABLE** | routing template `XMC-F-03` — *"make-or-buy on demand"* |
| 3 | **Source module responsibility** | **TRAVERSABLE** | Sales → Manufacturing |
| 4 | **State transition** — enter RM shortage | **TRAVERSABLE** | shortage state exists |
| **5** | **STATE TRANSITION — LEAVE shortage on procurement being raised** | **`BREAK`** | *"the shortage state exits **only on reservation completing, never on procurement being raised**. **A shortage can therefore be entered and never left by supply.**"* |
| 6 | Approval interaction | not reached | — |
| 7 | Posting interaction | not reached | — |
| 8 | Inventory / accounting impact | not reached | — |
| 9 | Event / immutable record | not reached | — |
| 10 | Downstream consumer | not reached | — |
| 11 | Reconciliation | not reached | — |
| 12 | Reversal / exception | not reached | — |
| — | **Final observable state** | **UNREACHABLE** | node 5 |

**`4 of 12` nodes traversable · `1` break · `7` unreachable because of it.**

---

## 2. What HAS changed since `PT-16` — and it is real

| Half of the break | State at `PT-16` | State now |
|---|---|---|
| **`C2-D-01`** soft-vs-hard fulfiller binding | Boss election, open | **RULED — `SOFT BINDING CONFIRMED`** (`SC-BD-02`) |
| **The missing procurement exit** | undetermined | **SPECIFIED** — `SC-01` §6.2: *"Specifying that the shortage state carries a **supply-raised exit** is an architecture act within SMEs Core authority, and **it is performed here as a specification requirement**"* |

> **Both halves of the two-clause break have been addressed: one ruled, one specified.**
> **And `E2E-04` is still `NOT TRAVERSABLE`, for a reason that is about authority, not evidence.**

---

## 3. `CC-F-08` — why the re-grade is barred, in the sources' own words

**Three records, all barring the same act:**

| Source | Words |
|---|---|
| **`SC-01` §6.2** (the session that wrote the specification) | *"it does **not** re-grade `E2E-04` to `TRAVERSABLE`. A prior round attempted that re-grade and **withdrew it under challenge**; **reversing a withdrawal that a challenge produced, on the strength of a specification this same session wrote, would be the self-interested-classification failure the programme has recorded.** The specification is published and **the re-grade is routed to SMT**"* |
| **`SC-BD-02` §8.4** (the Boss ruling) | *"**`E2E-04` is NOT re-graded `TRAVERSABLE` by this ruling.** A prior round attempted that and withdrew it under challenge; **the re-grade is held for the independent reviewer**"* |
| **`SA15` v2** (the register) | the re-grade was **withdrawn** by `CHF-03` after a draft **suppressed the second clause of its own source sentence** |

### 3.1 The same bar applies to this session, with the same force

> **This executor authored `PT-00`…`PT-17`. Re-grading `E2E-04` on the strength of a specification that
> SMEs Core wrote, over a withdrawal that a challenge produced, would be the identical self-interested
> classification — performed by a third party in sequence rather than by the original author.**

**`0` re-grade is made.**

### 3.2 A divergence in the routing, recorded not resolved

| Record | Routes the re-grade to |
|---|---|
| `SC-01` §6.2 | **SMT** (`SC-03`), *"which owns it"* |
| `SC-BD-02` §8.4 | **the independent reviewer** (B-7) |

**Both are current. Neither cites the other. The owner of the re-grade is therefore itself unsettled** —
recorded as a routing question for Boss, not adjudicated here.

---

## 4. Disposition

| | |
|---|---|
| **`E2E-04`** | **`NOT TRAVERSABLE` — `HOLD`** |
| Node that breaks | **`5`** — supply-raised exit from the shortage state |
| Break at **specification** level | **CLOSED** — `SC-01` §6.2 |
| Break at **target-model** level | **OPEN** — the state machine still has no supply exit |
| Break at **runtime** level | **OPEN** — no implementation |
| Re-grade authority | **SMT or B-7 — divergent (§3.2). NOT SMEs Core, and NOT this session** |
| Boss item | route the re-grade owner; then the owner re-grades or declines |

---

## 5. Checkpoint

> **`12`-node chain built: `4` traversable, **`1` break at node 5**, `7` unreachable · **both halves of the
> break have moved — `C2-D-01` RULED and the supply-raised exit SPECIFIED** · **the re-grade is barred to
> this session by three records and by the identical self-interest reasoning that produced the original
> withdrawal** · `CC-F-08` records a **divergence in who owns the re-grade** (SMT vs B-7) · **`E2E-04`
> remains `HOLD`; `0` re-grades made.**

