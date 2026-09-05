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

---

# RESTATED AFTER CROSS-PROCESS RECONCILIATION

**Correction `P10-R-09` applies to everything above this line.** The parent register routed the ledger, period close, the fiscal calendar and FX policy to `P04`, which is the **asset** process. The correct counterparties are `P08` for the ledger and `P09` for the analytic dimension. The parent rows are preserved as lineage; the routing below supersedes them.

## Restated Peer Dependencies

| # | Peer | What P10 needs | Status after reconciliation |
|---|------|----------------|------------------------------|
| `D-01` | `P01` | Definition of a purchased-service period on a bill line | `PEER DEPENDENCY OPEN` — unchanged |
| `D-02` | `P02` | Definition of a sold-service period; separation of billing period from recognition window | `PEER DEPENDENCY OPEN` — unchanged |
| `D-03` | `P02` | Whether the accrual measurement matches the revenue cut-off measurement | `PEER DEPENDENCY OPEN` — unchanged |
| `D-04` | ~~`P04`~~ → **`P08`** | The fiscal calendar and the civil-versus-fiscal grid ruling | **RE-ROUTED.** `P08` establishes the ledger has **no period object at all** — a period is a date range. So this is not merely open, it is **blocked on a ledger concept that does not exist** |
| `D-05` | ~~`P04`~~ → **`P08`** | Ruling that a posting constraint may not silently alter a recognition period | **RE-ROUTED and PARTIALLY RESOLVED.** `T0-13`'s close condition — refuse **or** record an attributable trace — is adopted programme-wide. The remaining choice is a Boss decision, classified in `28` |
| `D-06` | ~~`P04`~~ → **`P08`** | FX policy for a recognition event | **RE-ROUTED.** `PEER DEPENDENCY OPEN`; P10 has not reconciled against `P08`'s currency model — recorded as `D-13` |
| `D-07` | `P05` | Whether employee prepayments are P10 events | `PEER DEPENDENCY OPEN` — unchanged |
| `D-08` | `P06` | Whether bank-side interest accrual is a P10 event | `PEER DEPENDENCY OPEN` — unchanged |
| `D-09` | `P07` | Prepaid-versus-deferred presentation; reversing accrual across a tax period | `HOLD / EVIDENCE REQUIRED` — unchanged |
| `D-10` | `P11` | Ratification of P10's scope determinations | **PARTIALLY RESOLVED.** Three `P11`/`P09` positions adopted (`SCP-08`, `SCP-09`, `MA-11`). Line-by-line comparison against peer matrices is **class `C`, not performed** — `P10-U-21` |
| `D-11` | `P04` | Whether the asset object accepts shared ownership of allocation, identity and correction | **PARTIALLY RESOLVED.** No contradiction found on any fact; four independent agreements recorded. `P04`'s *kernel position* was not extracted — `PR-04-01` |
| `D-12` | Account Wave A | FX and accounting-date findings | Available; cited, not re-derived — unchanged |
| **`D-13`** | **`P08`** | The currency model for a programmatic entry carrying no currency of its own | **NEW.** P10's recognition lines carry none |
| **`D-14`** | **`P08`** | The accounting-event object and its identity (Boss `D-5`) | **NEW and GATING.** `P10-D-01` is now sequenced behind it |
| **`D-15`** | **`P09`** | The cost object, which does not exist as a first-class object | **NEW.** P10 cannot specify what a recognition event is attributed to |

## Dependency Arithmetic

| | Count |
|---|-------|
| Original (parent round) | 12 |
| **Resolved outright** | **0** |
| **Partially resolved** | **4** (`D-05`, `D-10`, `D-11`, and `D-12` which was already available) |
| **Re-routed to the correct peer** | **3** (`D-04`, `D-05`, `D-06`) |
| Remaining open | 8 |
| **Newly opened by the reconciliation** | **3** (`D-13`, `D-14`, `D-15`) |
| **Total open after reconciliation** | **11** |

The count went from 12 to 11 while four were partially resolved and three were newly opened. **Reconciliation reduced ambiguity far more than it reduced count** — three dependencies were pointed at the wrong process and would never have been satisfied, and three real ones were invisible until the correct peers were read.

## Obligations P10 Places on Peers — restated

| # | For | Obligation |
|---|-----|-----------|
| `E-01` | **`P08`** | Author the accounting-event object; P10 specialises rather than duplicates |
| `E-02` | **`P08`** | Provide somewhere to record the period an amount belongs to, distinct from the posting date |
| `E-03` | **`P08`** | On a constraint-driven date change: refuse, or record an attributable trace |
| `E-04` | **`P08`** | The nets-to-zero attribution and the untracked post-lock editability are posting-layer properties |
| `E-05` | **`P09`** | A second confirming instance of the attribution root cause, in a mechanism unrelated to assets |
| `E-06` | `P01` / `P02` | Record measurement rate and date alongside any recognition window |
| `E-07` | `P02` | Separate billing period, recognition window and statutory invoice period |
| `E-08` | **`P04`** | Independent confirmation of the silent re-dating from a second mechanism, plus the deployment fact that makes it live |
| `E-09` | `P11` | The event-identity forensic as input to `D-5`; the option classification as input to `D-12`/`T0-13`; correction `P10-R-09` |
| `E-10` | All peers who read the parent package | **`P10-R-09`** — the parent cross-process document routed ledger obligations to the asset process |

## Independence Statement — restated

Nothing in `01`–`09` or `22`–`33` depends on a peer's determination for its **facts**. What depends on peers is the **design decision**, and it now depends on `D-14` (`D-5`) rather than on the two dependencies the parent round named. `P10-D-01` is **not independently decidable** and must be sequenced after the accounting-event identity is authored.
