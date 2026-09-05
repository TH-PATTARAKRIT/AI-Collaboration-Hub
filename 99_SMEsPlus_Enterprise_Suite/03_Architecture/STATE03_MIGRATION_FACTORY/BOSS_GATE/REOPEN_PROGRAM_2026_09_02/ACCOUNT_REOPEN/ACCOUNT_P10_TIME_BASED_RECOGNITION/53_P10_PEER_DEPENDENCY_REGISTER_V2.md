# P10 — PEER DEPENDENCY REGISTER, VERSION 2

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D14`. **Rebuilt from the registers, not forced to a prior count.**

The prior round reported *"12 original → 11 remaining"*. Neither figure is carried. The population below is re-derived.

---

## 1. Peer Commits Consumed

| Peer | Last consumed (prior round) | Current head | Delta |
|------|----------------------------|--------------|-------|
| `P04` Acquire-to-Retire | `1636df4` | **`6953856`** | **10 commits** — consumed |
| `P08` Record-to-Report | `4bdf8a2` | `4bdf8a2` | **none — not reprocessed** |
| `P09` Plan-to-Analyze | `9a3bded` | **`70f8d20`** | **2 commits** — consumed |
| `P11` Central Reconciliation | `9b646a0` | **`6b028ea`** | **12 commits, deltas 03–10 plus corrections** — consumed |

## 2. The Register

| ID | Peer | What P10 needs | Status | Boss-dependent? | Expiry trigger |
|----|------|----------------|--------|-----------------|----------------|
| `PD-01` | `P01` | Definition of a purchased-service period on a bill line | **OPEN — PEER EVIDENCE** | no | — |
| `PD-02` | `P02` | Definition of a sold-service period; separation of billing period from recognition window | **OPEN — PEER EVIDENCE** | no | — |
| `PD-03` | `P02` | Whether the accrual measurement matches the revenue cut-off measurement | **OPEN — PEER EVIDENCE** | no | — |
| `PD-04` | `P08` | A period concept in the ledger, and the fiscal-versus-civil grid ruling | **OPEN — BOSS DECISION** | **yes** | — |
| `PD-05` | `P08` + Boss | Whether a posting constraint may alter a recognition period | **OPEN — BOSS DECISION**, coupled to `T0-13` | **yes** | — |
| `PD-06` | `P08` | Currency model for a programmatic entry carrying no currency | **OPEN — PEER EVIDENCE** | no | — |
| `PD-07` | `P05` | Whether employee prepayments are P10 events | **OPEN — PEER EVIDENCE** | no | — |
| `PD-08` | `P06` | Whether bank-side interest accrual is a P10 event | **OPEN — PEER EVIDENCE** | no | — |
| `PD-09` | `P07` | Prepaid-versus-deferred presentation; reversing accrual across a tax period | **OPEN — PEER EVIDENCE**, `HOLD / EVIDENCE REQUIRED` | no | — |
| `PD-10` | `P11` | Ratification of P10's scope determinations | **PARTIALLY RESOLVED** — three peer positions adopted; line-by-line comparison not performed | no | see `55` |
| `PD-11` | `P04` | Whether the asset process accepts shared ownership of allocation, identity and correction | **PARTIALLY RESOLVED** — no factual contradiction; kernel position not extracted | no | — |
| `PD-12` | Account Wave A | FX and accounting-date findings | **RESOLVED** — available, cited, not re-derived | no | — |
| `PD-13` | `P08` | Currency model for recognition lines carrying no currency | **OPEN — PEER EVIDENCE** | no | — |
| `PD-14` | `P08` / Boss | The accounting-event object and its identity (`D-5`) | **OPEN — BOSS DECISION** · **GATING** | **yes** | `AASP-COND-01` |
| `PD-15` | `P09` | The cost object, which does not exist as a first-class object | **OPEN — PEER EVIDENCE** | no | — |
| **`PD-16`** | `P11` | **`T0-13` / `P11-B-16` — status confirmed `HOLD — BOSS DECISION REQUIRED`; close condition **refined** so a trace is mandatory where no violation exists** | **OPEN — BOSS DECISION** · **GATING** · **NEW this round** | **yes** | — |
| **`PD-17`** | `P11` + `P08` | **The lock-free mutation path — its population in P10's mechanisms** | **OPEN — CROSS-PROCESS CONTRADICTION** · **NEW** | no | — |
| **`PD-18`** | `P04` | **Whether the asset line's real-asset population is zero in the newer product line** — P04 asserts it; P10 verified it from its own extracts | **RESOLVED — this round** | no | — |

## 3. Arithmetic — with the unit declared

**Unit: one distinct dependency of P10 on a party outside P10.**

| Class | Count |
|-------|-------|
| **Total population** | **18** |
| RESOLVED | **2** (`PD-12`, `PD-18`) |
| PARTIALLY RESOLVED | **2** (`PD-10`, `PD-11`) |
| RE-ROUTED (carried from the prior round's taxonomy correction) | 3 — now shown at their corrected peer and **not counted again** |
| OPEN — PEER EVIDENCE | **9** |
| OPEN — BOSS DECISION | **4** (`PD-04`, `PD-05`, `PD-14`, `PD-16`) |
| OPEN — CROSS-PROCESS CONTRADICTION | **1** (`PD-17`) |
| SUPERSEDED | 0 |
| **NEW this round** | **3** (`PD-16`, `PD-17`, `PD-18`) |
| **Remaining open** | **14** |

**The prior round's "12 original / 11 remaining" is not carried.** It was built on the mis-assigned taxonomy and on a partition that double-counted one item. The population is **18**, of which **14 are open**.

**The count went up because the round found more, not because more was created.** Two dependencies were resolved and three discovered.

## 4. `P11` Impact

| Dependency | What P11 must carry |
|------------|---------------------|
| `PD-05` + `PD-16` | Present as **one coupled decision**, `T0-13` first — `40` |
| `PD-14` | `D-5`, with P10's acceptance condition attached |
| `PD-17` | The lock-free path is **not** disposed of by a ruling on the lock path |
| `PD-10` | Scope comparison remains class `C` — `55` |
