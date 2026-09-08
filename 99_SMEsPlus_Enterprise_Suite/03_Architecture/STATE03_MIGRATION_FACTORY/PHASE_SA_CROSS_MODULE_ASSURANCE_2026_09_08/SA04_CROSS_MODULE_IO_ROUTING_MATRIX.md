# SA04 — CROSS-MODULE INPUT/OUTPUT ROUTING MATRIX
## CP-SA-30 — OUTPUT AND ROUTING COMPLETENESS

Status: **HOLD**
Inputs: `SA02`, `SA03`. Evidence: Group A cross-module event and dependency map
(`8b0993d8`), Account P-series handoffs, Boss decisions on `origin/SMEsPlus` `fa57d10f`.

---

## 1. Producer → consumer routing table

Coupling classes used below, taken from the evidence rather than imposed:

| Class | Meaning |
|---|---|
| `HARD` | The consumer's process cannot proceed correctly without it |
| `ADVISORY` | Read and displayed, but nothing blocks on it |
| `WRITE` | The producer creates or mutates a record inside the consumer |
| `ROUND-TRIP` | A produces to B, then reads B's result back to derive its own state |

| # | Producer | Output | Consumer | Class | Status |
|---|---|---|---|---|---|
| R-01 | Sales | commitment confirmed | Inventory | `HARD` (indirect, via rule engine) | evidenced |
| R-02 | Sales | line quantity changed on a confirmed commitment | Inventory | `HARD` | evidenced |
| R-03 | Sales | quantity reduced below delivered | Inventory | **blocked** for stock-tracked lines; user redirected to the return route | evidenced |
| R-04 | Sales | commitment cancelled | Inventory | `HARD` | evidenced, closed under Group A CORR-003 |
| R-05 | Sales | billable-now quantity | Accounting | `HARD` | evidenced |
| R-06 | Accounting | billing posted | Sales | `ROUND-TRIP` | evidenced |
| R-07 | Sales | subcontract-service line confirmed | Purchase | **`WRITE`** | evidenced — the only boundary write; see `SA03-F-02` |
| R-08 | Purchase | commitment confirmed / approved | Inventory | `HARD` (direct, synchronous) | evidenced |
| R-09 | Purchase | commitment cancelled | Inventory | `HARD`, state-partitioned by receipt scenario | evidenced, closed under CORR-003 |
| R-10 | Purchase | billable-now quantity | Accounting | `HARD` | evidenced |
| R-11 | Accounting | supplier billing posted | Purchase | `ROUND-TRIP` | evidenced |
| R-12 | Demand request | approved | Purchase | `HARD` gate on conversion | evidenced |
| R-13 | Inventory | movement completed | Sales (delivered), Purchase (received) | `HARD` input to the next gate | evidenced |
| R-14 | Inventory | availability / forecast | Sales, Purchase | `ADVISORY` | evidenced as advisory-only |
| R-15 | Inventory | replenishment threshold fired | Purchase | `HARD`, one-way reflective | evidenced, closed under CORR-003 |
| R-16 | Inventory | movement reserved | Sales widgets | `ADVISORY`; **no equivalent read path on the buy side** | evidenced |
| R-17 | Inventory | remaining-supply record created | *nobody* | — | `NO CONSUMER` |
| R-18 | Inventory | return created | Sales, Purchase re-stamp links; neither initiates | `ADVISORY` | evidenced |
| R-19 | Accounting | tax determination | Sales, Purchase | `HARD` — neither computes tax itself | evidenced |
| R-20 | Accounting | customer-invoice lifecycle state | Sales cancellation gate | `HARD` **required, no contract** | **`XD-01`** |
| R-21 | Manufacturing | production consumption / FG receipt | Inventory | `HARD` | evidenced via P03 |
| R-22 | Manufacturing | production cost elements | Accounting | `HARD` | `GAP` — fixed-overhead elements without an injection path (P03) |
| R-23 | Asset | capitalization from a posted vendor bill | Accounting | `HARD` | evidenced via P04 |
| R-24 | Equipment | availability / breakdown | Manufacturing work order | `HARD` per Boss `a11c9e7b` §3 | **`HOLD`** — SA-D20 thin |
| R-25 | Quality | inspection outcome | Inventory availability, cost timing | `HARD` | **`HOLD`** — SA-D19 thin |
| R-26 | Project | operational progress | Analytic dimension | `HARD` per Boss `fa57d10f` | **`HOLD`** — SA-D18 thin |
| R-27 | Service | completion evidence | Accounting recognition | `HARD` | **`HOLD`** — SA-D17 thin |
| R-28 | Supply routing | resolved Supply Nature | every downstream route | `HARD` | **`HOLD`** — `SA05-F-02` |

### 1.1 Routing completeness count

| Class | Rows |
|---|---|
| Evidenced and compatible | 20 |
| No consumer identified | 1 (R-17) |
| Gap | 1 (R-22) |
| `HOLD` — thin domain or undetermined | 6 (R-24…R-28, plus R-20 contradiction) |
| **Total routes** | **28** |

**20 of 28 cross-module routes are evidenced.** Eight are not, and seven of those eight trace to
the five thin domains and the one contradiction already registered.

---

## 2. SA04-F-01 — the routing graph has a hole exactly where the ledger is not involved

~~Every route with an Accounting endpoint is evidenced~~ **(CORR2 `K2-09`)** — the universal is
withdrawn: it is broken by R-27 Service→Accounting **in the same paragraph** as it is asserted, and
by R-20 and R-22, which this sentence itself excepts. The supportable statement is that **routes
with an Accounting endpoint are evidenced more often than routes between two operational modules**
(R-05, R-06, R-10, R-11, R-19, R-23 evidenced; R-20, R-22, R-27 not).

Every route between two **operational** modules that is not on the accounting path is `HOLD`:
Equipment→Manufacturing (R-24), Quality→Inventory (R-25), Project→Analytic (R-26),
Service→Accounting (R-27).

~~This is `SA00-F-01` seen a second way … Two independent measurements agreeing is worth more than
one measurement repeated~~ — **WITHDRAWN by CORR2 `K2-09`.** The two measurements are **not
independent**: this matrix inherits `SA01`'s domain classification and `SA05`'s nature list, and
`SA_CORR2_03` §1 establishes that both rest on **an undeclared pattern**. They are one unpublished
search read twice. The observation itself — that the evidence follows the money — survives on the
strength of `SA00` §7's published operational-versus-accounting term contrast, which is a genuinely
separate instrument; the *convergence* claim does not.

## 3. SA04-F-02 — five of nineteen evidenced routes were closed by a correction, not by the original research

R-04, R-09, R-15 and the two event findings behind R-13 were all recorded as gaps by the
original Group A research and closed only by the CORR-003 / CORR-010 corrective cycles and
confirmed by independent re-verification RV-011 (`77e93d44`).

Phase SA records this because it bears on how much confidence the remaining nine unevidenced
routes deserve: in this programme, **the first pass over a cross-module route found a gap more
often than it found a clean route**, and independent re-performance was what settled them.

## 4. Conditional routing — automatically created routes (master prompt AUTO-04)

Where one output has several consumers, all relevant downstream routes are created rather than
the primary one only:

| Output | All routes created |
|---|---|
| Completed movement | → Sales delivered · → Purchase received · → product-level on-hand and forecast · → Accounting (cost/COGS, via valuation policy) |
| Commitment cancelled | → Inventory transfer cancellation · → Accounting reversal event under BD-ACC-01 · → the sell-side gate question `XD-01` |
| Billing posted | → source-module already-billed derivation · → AR/AP ageing · → payment matching · → tax register |
| Production completed | → FG into Inventory · → cost into Accounting · → variance into Accounting · → Equipment usage/meter (`HOLD`) |

---

`CP-SA-30 — HOLD`. Outputs, consumers and conditional routes are mapped; 20 of 28 routes are
evidenced, and the eight that are not are individually named and routed.

Boss remains the sole Final Approver.
