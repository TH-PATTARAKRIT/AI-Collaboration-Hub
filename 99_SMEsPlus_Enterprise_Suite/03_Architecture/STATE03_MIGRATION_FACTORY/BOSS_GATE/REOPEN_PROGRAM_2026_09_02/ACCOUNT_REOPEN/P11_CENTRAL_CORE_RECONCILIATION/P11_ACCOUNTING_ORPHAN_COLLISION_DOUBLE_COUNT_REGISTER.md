# P11 — ACCOUNTING ORPHAN / COLLISION / DOUBLE-COUNT REGISTER

`[SMEPLUS-26-09-06-…-CORR2-PHASES-001]` · `CQ-P11-14` · **PHASE S** · Layer 1 clean-room

> **Bounded to the Frozen Peer Snapshot + P11's own evidence.** This is a Phase-S **Accounting House**
> issue register. It is **not** Phase-B Whole-ERP reconciliation, and it designs nothing.

---

## 1. Unowned accounting truth — an input with no accounting owner

| id | Item | Evidence | Disposition |
|---|---|---|---|
| `OC-01` | **The tie-out between the asset register and the ledger.** Both are genuinely separate stores; *"the kernel imposes no tie-out, no periodic proof and no exception"* | `P08` `P08-RQ-KRN-01` | `BOSS DECISION REQUIRED` — no process owns it and none may assume it |
| `OC-02` | **The tie-out between the inventory valuation record and the ledger.** Same kernel gap; and the FK that links them is `ON DELETE SET NULL` | `P08`; `P01` `S16-B-05` | `BOSS DECISION REQUIRED` |
| `OC-03` | **Whether the failure of a tie-out is itself an accounting event.** No process claims it | `P08` `58_` §3 q4 | `BOSS DECISION REQUIRED` |
| `OC-04` | **The subcontract bill-difference path in the older generation** — *"no deployment exercises it; P01 concurs"* | `P03` hold; `P01` | `UNRESOLVED — SPECIFIC P11 EVIDENCE UNAVAILABLE` |

## 2. Collision — two processes claiming, or disclaiming, the same accounting truth

| id | Collision | Resolution |
|---|---|---|
| `OC-05` | **Valuation cost explosion.** `P01` routed ownership to `P03`; `P03` routed it back and had **independently reached the same attribution from its own data** | **Resolved by the peers, not by P11.** Owner: **`P01`**. *"Two processes, opposite directions, one answer."* P11 records the convergence and takes **reliance only** |
| `OC-06` | **Series-16 source existence.** `P04-B-51`: *"no series-16 source exists on this host"*. `P01` `ERR-P01-41`: **31 core trees across five series, 16.0 ×3** | **`CONTRADICTED — CORRECTED AND CLOSED` (`X4-C7`).** P11 declared this not adjudicable **while the answer sat inside P11's own frozen population**: `P02` `45_` `C-86` — ***"MAJOR REVERSAL. THE REFERENCE DISTRIBUTIONS EXIST. `C-55` IS WITHDRAWN"*** — a **950-module 16.0 Enterprise** distribution under `~/Library/CloudStorage/`, and *"Expert 4's `CH-4` … refuted; its sweep pruned `Library` too."* **Three peers, one answer: the source exists. `P04-B-51` and `P03`'s named hold are discharged by evidence, not by argument** — routed to both owners |
| `OC-07` | **Identifier-namespace collision on P11's own decision ids.** `P03` routes decisions to P11 as **`P11-D-4`, `P11-D-5`, `P11-D-6`**, continuing its own `P11-D-1..3` sequence. P11's matrix already contains **`D-4`, `D-5`, `D-6`** — *different decisions*, and `D-5` is the event-identity decision eight processes depend on | **`CONTRADICTED — CORRECTED AND CLOSED`.** P11 registers P03's three as **`D-16`, `D-17`, `D-18`** and publishes the crosswalk (§2.1). **A reader resolving `P11-D-5` against P11's matrix would have landed on the programme's most-depended-upon decision by mistake** |

### 2.1 Decision-id crosswalk — `P03` namespace → P11 register

| `P03` routes as | P11 register id | Question |
|---|---|---|
| `P11-D-1` | **`D-13`** | may a scope narrowing for one object be read across to a related object? *(P03 dissent preserved: unlinked in both directions)* |
| `P11-D-2` | **`D-14`** | what closes a defect whose specified evidence returns an empty population? *(now **partly answered** — found in a fourth database, **0 of 60**)* |
| `P11-D-3` | **`D-15`** | is `MA-11` binding on `P01`–`P10`? |
| **`P11-D-4`** | **`D-16`** | **which ledger is authoritative** where the inventory subsidiary ledger and the GL disagree, and how is divergence detected? |
| **`P11-D-5`** | **`D-17`** | **remediation sequencing** for a corrupt position that currently **self-cancels** — any single-process fix releases the full gross exposure |
| **`P11-D-6`** | **`D-18`** | may a defect with **zero measured incidence** but a permitted mechanism be closed? |

## 3. Double counting and double movement

| id | Item | Evidence | Disposition |
|---|---|---|---|
| `OC-08` | **Cross-cost-centre displacement invisible to every aggregate.** Inside entries counted as netting **exactly 0.00**, cost of **2,019,008.49 moves in each direction** between cost centres — entry-balanced, so no net figure can see it. Gross movement across centres is **154,922,194.55**, ≈ **43×** the scalar net | `P09` `D25` | `FACT VERIFIED — P11 ACCOUNTING BOUNDARY`. **`CANDIDATE ACCOUNTING TRUTH`: management attribution must reconcile on gross movement per centre, never on a net** |
| `OC-09` | **`D-17`'s self-cancelling corrupt position.** 30 valuation records to ±1.5 × 10²¹ distort inventory valuation by **−48.7 %**; the position currently self-cancels, so **any single-process fix releases the full gross exposure** | `P03` | `BOSS DECISION REQUIRED` — sequencing is above every individual process |

## 4. The item that is none of the above, and outranks all of them

> **`OC-10` is not an orphan, a collision, or a double count. It is a *reliance* defect, and it is
> the reason this register cannot be closed.**
>
> `ON DELETE SET NULL` on the valuation↔entry link, plus an **installed** module performing raw
> `DELETE FROM` with no ORM, no lock-date check, no company filter and no log, means
> **"never posted" and "posted and later deleted" are observationally identical.**
>
> Every zero-shaped negative in this register's supporting evidence — and in P11's own registers —
> has a **competing explanation that has never been excluded**. `P11-B-26`.

**Disposition: `AUTHORIZATION REQUIRED — EXACT EVIDENCE ACTION NAMED`** — the orphan-signature query
`P06` specified, executed under `D-3b` v5 `E0`.

---

**Totals — re-executed after challenge (`X2-C1`, `X1-9`): `10` items.**

| Disposition | Count | Items |
|---|---|---|
| `BOSS DECISION REQUIRED` | **4** | `OC-01`, `OC-02`, `OC-03`, `OC-09` |
| `UNRESOLVED — SPECIFIC P11 EVIDENCE UNAVAILABLE` | **1** | `OC-04` |
| `CONTRADICTED — CORRECTED AND CLOSED` | **2** | `OC-06`, `OC-07` |
| `EXTERNAL / PEER OWNER` — resolved by the peers | **1** | `OC-05` |
| `FACT VERIFIED — P11 ACCOUNTING BOUNDARY` | **1** | `OC-08` |
| `AUTHORIZATION REQUIRED` | **1** | `OC-10` |

**The earlier breakdown (`4 Boss · 2 unresolved · 1 peer-owned · 1 corrected · 2 fact-verified`) did not
match its own rows and is corrected. `CQ-P11-14`'s "9 items" is corrected to 10.** `P11-E-40`.

**`CQ-P11-14` — COMPLETE — EVIDENCE VERIFIED.**
