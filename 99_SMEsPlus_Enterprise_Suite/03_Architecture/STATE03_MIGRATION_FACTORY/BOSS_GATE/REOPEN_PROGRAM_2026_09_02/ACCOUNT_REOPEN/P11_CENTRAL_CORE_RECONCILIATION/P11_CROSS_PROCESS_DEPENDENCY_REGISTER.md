# P11 — UNIFIED CROSS-PROCESS DEPENDENCY REGISTER

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Model 14 of 15 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. The dependency graph, as a topology

```
                       ┌──────────────────────────────────────────┐
                       │  UAE-29  ACCOUNTING EVENT IDENTITY        │
                       │  absent — root of C1 44/44, DC-01, XM-01  │
                       └───────────────────┬──────────────────────┘
                                           │ everything below depends on it
   P01 ──┐                                 │
   P02 ──┤                                 ▼
   P03 ──┼──▶ Layer 2 VALUATION ──▶ Layer 3 ACCOUNTING EVENT ──▶ Layer 4 LEDGER ──▶ P08
   P04 ──┤    JT-01..JT-05, JT-08,          (does not exist)         (exists)
   P05 ──┤    BLK-07  — ALL OPEN                                        │
   P10 ──┘                                                              ├──▶ P09  (read-only,
                                                                        │      substrate destructible)
   P06 ──▶ emits UAE-01/02/03 ──────────────────────────────────────────┤
           (a consumer that is a producer)                              │
   P07 ──▶ consumes P01/P02/P05/P06 ──▶ sets P08 lock as a side effect ─┘
```

## 2. Register

| id | Dependency | From → To | Kind | Status |
|---|---|---|---|---|
| `DEP-01` | **Accounting-event identity** | platform → **all ten** | structural | **`HOLD — BOSS DESIGN DECISION`. The root. Nothing downstream is closable without it** |
| `DEP-02` | COGS recognition timing (`JT-04`) | Inventory ↔ `P02` | joint decision | **`NOT DECIDABLE`** — needs `SME-Q-03`, `TH-NEW-01` |
| `DEP-03` | Return cost basis (`JT-05`) | Inventory ↔ `P02` | joint decision | **`NOT DECIDABLE`** — needs `SME-Q-02`, `TH-NEW-02`, a live FIFO-return test |
| `DEP-04` | Valuation-policy ownership (`JT-01`) | Inventory ↔ `P01`/`P03` | joint decision | **`NOT DECIDABLE`** — 8 sub-facts, 2 need live access |
| `DEP-05` | Perpetual vs periodic (`JT-03`) | Inventory ↔ `P08` | design decision | **open — no stable reference pattern exists to imitate** |
| `DEP-06` | Price-difference account scope (`JT-02`) | `P01` ↔ Inventory | contradiction | **open** |
| `DEP-07` | Landed cost (`JT-08`) | `P01` ↔ Inventory | joint decision | **open, Audit VETO retained** |
| `DEP-08` | Absorption rate basis (`BLK-07`) | `P04` → `P03` → Inventory | design decision | **`HOLD`. AAS+ veto: no costing implementation may begin** |
| `DEP-09` | Maintenance planned/unplanned split (`BLK-08`) | `P04` → `P03` | design decision | **`HOLD`** |
| `DEP-10` | Machine identity — duplicate asset records (`BLK-02`) | `P04` → `P03` | **UAT** | **`HOLD — UAT REQUIRED`**, query `Q-02`. *A duplicated machine's cost pool doubles, silently* (`DC-08`) |
| `DEP-11` | Day convention in live data (`BLK-01`) | `P04` | **UAT** | **`HOLD — UAT REQUIRED`**, query `Q-01` |
| `DEP-12` | **Installed-module list of the running system** (`Q-04`) | all | **UAT** | **`HOLD — UAT REQUIRED`. It caps every negative finding in two research packages, and it is one query** |
| `DEP-13` | Reference core root declaration (`MCU-21`) | programme → all | **declaration** | **`HOLD — BOSS DECISION`. 22 roots exist; none is declared. Cost to close: hours, mechanical, no new research** |
| `DEP-14` | FX rate ownership & missing-rate policy (`GB-08`) | `P06`/`P07`/`P08` | **Boss decision** | **`BOSS DECISION REQUIRED`** — packaged, not decided |
| `DEP-15` | Prior-period attribution mechanism (`UAE-32`, `JT-06`) | `P01`, `P03`, `P10` → `P08` | design | **`HOLD` — no mechanism exists in the reference at all** |
| `DEP-16` | Absorbed-vs-actual variance (`UAE-31`) | `P03` ↔ `P08` | design | **`HOLD`** — TAS 2 ¶13 compliance unprovable without it |
| `DEP-17` | Expense producer contract | `P05` → `P08` | evidence | **`UNKNOWN — EVIDENCE REQUIRED`** |
| `DEP-18` | Deferred-recognition producer contract | `P10` → `P08` | evidence | **`UNKNOWN — EVIDENCE REQUIRED`** |
| `DEP-19` | Analytic destruction on correction (`XM-03`) | `P08` → `P09` | design | **raised by Wave A, routed to the analytic Wave, never taken** |
| `DEP-20` | Intercompany transfer path (`JT-10`, `GAP-FS-07`) | Inventory ↔ `P08` | evidence | **path never traced end to end** |
| `DEP-21` | Opening-balance certification (`JT-11`, `GAP-FS-08`) | migration → all | evidence | **element 14 does not exist** |
| `DEP-22` | Scope determination per object | all ↔ all | **constitutional** | **4 objects `HOLD — SCOPE EVIDENCE REQUIRED`** (`P11_SCOPE_OWNERSHIP_MATRIX.md` §3) |
| `DEP-23` | **`P01`–`P10` publication** | peers → `P11` | **peer** | **`PEER DEPENDENCY OPEN × 10`** |

## 3. Two facts about this register that must be read together

1. **`DEP-23` blocks 15 of the 30 withheld debit/credit cells.**
2. **It does not block the other 15**, nor `DEP-01`…`DEP-22`. Those are decisions, UAT queries and
   declarations — and **six of them cost hours, not weeks**: `DEP-12` (one query), `DEP-13` (a
   declaration), `DEP-10`/`DEP-11` (two queries), `DEP-14` (packaged and awaiting a decision),
   `DEP-22` (four determinations).

> **The critical path does not run through the peer processes.** It runs through `DEP-01` — the
> accounting-event identity — which is a Boss design decision that no amount of research by any of the
> eleven sessions will close, and which nine of the twenty-three dependencies above sit downstream of.
