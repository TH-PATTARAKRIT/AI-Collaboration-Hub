# P11 — C8 · CONTINUOUS PEER DELTA INTAKE

`[SMEPLUS-26-09-05-ACC-P11-CORE-RECON-CORR1-001]` · CP-P11C08 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**
> **Delta-first: unchanged peers are not reread. Six peers had never been consumed at all.**

---

## 1. SHA state — last consumed vs current

| Peer | Last consumed by P11 | Current | State |
|---|---|---|---|
| `P01` Procure-to-Pay | **never** | `49d0fe3` | **NEW — 48 files** |
| `P02` Order-to-Cash | **never** | `06c5ed8` | **NEW — 30 files** |
| `P03` Manufacture-to-Cost | `812cc5c` | `7fca09a` | **CHANGED** |
| `P04` Acquire-to-Retire | `c839bfe` | `c57d846` | **CHANGED** |
| `P05` Expense-to-Pay | **never** | `808b30e` | **NEW — 67 files** |
| `P06` Bank-to-Reconcile | `4146bb1` | `9e5d729` | **CHANGED** |
| `P07` Tax-to-Compliance | `ecc6059` | `547b774` | **CHANGED** |
| `P08` Record-to-Report | **never** | `838134f` | **NEW — 60 files** |
| `P09` Plan-to-Analyze | **never** | `c029df3` | **NEW — 92 files** |
| `P10` Time-Based Recognition | **never** | `284ea66` | **NEW — 86 files** |

> ### `PEER DEPENDENCY OPEN × 10` → **`0`. All ten have published.**
> **Six were never consumed** — the `P11-F-12` distortion, now measured: P11 wrote nine deltas against
> the four peers that published first.

**Intake unit, declared:** the `CORE_RECON_HANDOFF_PACK` — the artefact each peer wrote **for P11**.
All ten exist. Full packages are **not** reread; deltas below are drawn from the pack each peer
designates as its handover.

## 2. Delta classification

| Peer | Class | Material content |
|---|---|---|
| **`P08`** | **STRENGTHENS + CHANGES BOSS PACKAGE** | **The root set is declared** (22, independently reproduced) — discharges the mechanical half of `D-1`. **Accounting-event identity: `A VERIFIED ABSENCE` across all 22 roots** — upgrades `UAE-29`/`T0-08`/`D-5` from class `C` to `A`. **No DB constraint enforces the balance invariant in any of the 22 roots** — strongest form of `T0-12`. **22 orphan/duplicate attacks, none stopped outright** — corroborates `0 of 17`. **The GL is a *reading*, not a store**; the fixed-asset register and inventory valuation record **are** stores and **nothing reconciles either to it** |
| **`P02`** | **STRENGTHENS + NEW REQUIREMENT** | **`P02-R-01`, the obligation ledger** — one row per unit that physically left, consumed by billing, cost taken from the row, relieved once and attributed once, enforced structurally. **Resolves six defects at root**, including P11's `DC-03` double COGS and `DC-04` double revenue. *"If the quantity behind billing and the quantity behind outflow diverge, cost of sales becomes an estimate — and gross margin is unauditable"* |
| **`P01`** | **CONTRADICTS / RESCOPES** | **The deployed v19 databases have no goods-received clearing account and no valuation-layer table.** The GRNI bridge is a **v18** mechanism; **two of three readable live databases cannot run it.** Core Accounting *"should not reconcile against a mechanism until `DEP-P01-01` establishes which generation is the subject"* — **this is `D-1`'s generation question arriving as a live blocker on P11's own matrix** |
| **`P09`** | **STRENGTHENS + NEW BLOCKER** | **Two of eight constitutional trace steps — financial-event identity and cost object — have no carrier at all**, so the trace *"must be authored"*. A management allocation on a posted, lock-dated, hash-chained entry **is changeable by an ordinary billing role with no audit trace**, and every budget figure over that period changes silently. Widens `B-11` beyond *"not a subledger of record"* |
| **`P10`** | **STRENGTHENS `T0-13`** | *"A recognition event is not a journal entry"* — the same layer-3 collapse. **A locked-period recognition entry is silently re-dated**, so `T0-13`'s mechanism reaches `P10` as well as `P01`/`P03`/`P04`. Scope: **service window is a tenant fact; the period grid is a company fact** |
| **`P05`** | **CONFIRMS + FILLS A GAP** | Discharges `B-12`'s `P05` half. **An advance is an asset**; employee and supplier obligations are **distinct in the ledger**; **authorising ≠ recording**; *"a control that cannot be shown to execute is not a control"*; statutory reference **platform-scoped**, its mapping company-scoped |
| **`P03`** | **CHANGED — no new material P11 impact** | Prior intake (`DC-09`, nine monetisations, behaviours 1–9) stands. Delta is internal repair |
| **`P04`** | **CHANGED — confirms** | `P04-F-66`/`B-31` compound already intaken; `F-78` withdrawn by its author; the stale joint figure struck |
| **`P06`** | **CHANGED — confirms** | Seven confirmed defects already intaken; identity system *"fails open at every layer"* stands |
| **`P07`** | **CHANGED — narrows, then strengthens** | `P07-F-60` **withdrawn** (5,201 certificates existed); replaced by `P07-F-62`, **stronger than the negative was**. `P07-F-03` constrained, not withdrawn |

## 3. What this changes in P11's own model

| P11 artefact | Change |
|---|---|
| `UAE-29` / `D-5` / `T0-08` | **class `C` → class `A`** over a declared root set (`P08`) |
| `D-1` | mechanical half **discharged** (`P08`); Boss half isolated |
| `T0-12`, `T0-11`, `T0-03`, `T0-01` | **strengthened** to their maximum available form (`P08`) |
| `T0-13` | **strengthened** — reaches `P10` (`P10`) |
| `DC-03`, `DC-04` | a **root-level remedy now exists** (`P02-R-01`) |
| `B-11` | **widened** — two trace steps have no carrier (`P09`) |
| `B-01`, `B-12` | **discharged** |
| `B-13` | **actionable for the first time** |
| **NEW** | **`P11-B-20`** — see §4 |

## 4. `P11-B-20` — a contradiction P11 must not resolve

> **`P01` says the bridge P11's event-to-GL matrix assumes is a v18 mechanism that two of three
> readable deployed databases cannot run.** P11's matrix, and every producer row in it, is written
> against a generation **nobody has declared**.

**This is not a P11 error** — the matrix withheld its producer cells precisely because the posting
patterns were unowned. **But it means the matrix cannot be populated by any peer until `D-1`'s
generation half is ruled**, and `P01` says so in terms. Registered **`P11-B-20`,
`HOLD — BOSS DECISION REQUIRED`**, routed to `D-1`.

## 5. Position

**10 of 10 consumed · 6 first-time · 4 delta-only · 0 rereads of unchanged material.**
**5 peers strengthen P11 · 1 contradicts/rescopes · 3 confirm · 1 narrows-then-strengthens.**
**2 blockers discharged · 1 opened · 0 closed by argument.**
