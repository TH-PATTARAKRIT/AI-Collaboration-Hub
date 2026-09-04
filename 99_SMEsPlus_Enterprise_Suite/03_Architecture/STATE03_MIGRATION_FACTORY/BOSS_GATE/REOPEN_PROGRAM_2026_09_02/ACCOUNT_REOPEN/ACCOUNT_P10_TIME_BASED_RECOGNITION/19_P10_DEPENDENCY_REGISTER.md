# P10 — DEPENDENCY REGISTER

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1
Issued under `SMEPLUS-26-09-04-ACC-REV2-CORR1` §6 and §7. A peer's incompleteness does not stop this session; it is recorded and unaffected work continues.

---

## 1. Peer Dependencies

| # | Peer | What P10 needs | Blocks what | Status |
|---|------|----------------|-------------|--------|
| `D-01` | `P01` P2P | Canonical definition of a purchased-service period on a bill line | Deferred expense trace finalisation | `PEER DEPENDENCY OPEN` |
| `D-02` | `P02` O2C | Same for sold services; separation of billing period from recognition window | `Y-04`; the semantic-overload remedy | `PEER DEPENDENCY OPEN` |
| `D-03` | `P02` O2C | Whether the accrual's delivered-not-invoiced measurement is the same as O2C's revenue cut-off measurement | `P10-D-03` (accrual ownership) | `PEER DEPENDENCY OPEN` |
| `D-04` | `P04` A2R | Fiscal calendar object; civil-versus-fiscal grid ruling | Kernel period-grid design | `PEER DEPENDENCY OPEN` — **gating** (`P10-U-13`) |
| `D-05` | `P04` A2R | Ruling that a posting constraint may not silently alter a recognition period | Kernel's load-bearing element | `PEER DEPENDENCY OPEN` — **gating** (`P10-U-14`) |
| `D-06` | `P04` A2R | FX policy for a recognition event; interaction with the Wave A finding of a silent one-to-one rate fallback | `P10-F-04` remedy | `PEER DEPENDENCY OPEN` |
| `D-07` | `P05` E2P | Whether employee prepayments are P10 events | Scope boundary | `PEER DEPENDENCY OPEN` |
| `D-08` | `P06` B2R | Whether bank-side interest accrual is a P10 event | Scope boundary | `PEER DEPENDENCY OPEN` |
| `D-09` | `P07` Tax TH | Prepaid-versus-deferred presentation; reversing accrual across a tax period | Presentation design only | `HOLD / EVIDENCE REQUIRED` — routed |
| `D-10` | `P11` | Ratification of P10's scope determinations | Nothing in P10; P11 reconciles continuously | `PEER DEPENDENCY OPEN` |
| `D-11` | Asset programme | Whether the asset object accepts kernel ownership of allocation, identity and correction | Kernel adoption, not kernel design | `PEER DEPENDENCY OPEN` |
| `D-12` | Account Wave A | The FX and accounting-date findings already established there | Consistency of `P10-F-04` and `P10-F-05` with the core ledger findings | Available; cited, not re-derived |

## 2. Dependencies P10 Creates for Others

| # | For | Obligation P10 imposes |
|---|-----|------------------------|
| `E-01` | `P04` A2R | Accept a recognition event carrying its own period as a ledger input |
| `E-02` | `P04` A2R | Make a re-dated posting produce a reportable divergence rather than a silent change |
| `E-03` | `P01` / `P02` | Record measurement rate and date alongside any recognition window |
| `E-04` | `P02` O2C | Separate billing period, recognition window and statutory invoice period into three fields |
| `E-05` | `P11` | Reconcile P10's PLATFORM assignments (convention definitions, grid algorithm, event schema) against the other processes' assignments |
| `E-06` | Whoever owns the accrual after `P10-D-03` | Provide a reproducible, stored measurement — the reference product's is computed in memory and discarded |

## 3. Independence Statement

Nothing in `01`–`09` depends on a peer's determination. The traces, matrices and registers are bounded to reference-ERP behaviour and to P10's own semantics. What depends on peers is the **design decision** (`P10-D-01`), and only through `D-04` and `D-05`.

This session therefore continues to its terminal state with twelve peer dependencies open, as `REV2-CORR1` §7 directs.
