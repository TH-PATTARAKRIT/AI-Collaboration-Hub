# P03 ← P01 FINAL HANDOFF INTAKE

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P03-01` precondition. **P01 was not executed or reopened.**

---

## 1. Exactly what was consumed

| Field | Value |
|---|---|
| P01 authoritative closure commit | **`b820b29b13f351ec21c724c05ea9aa8da2a15e14`** — verified present, and verified to be the **tip** of `origin/research/account-p01-procure-to-pay-2026-09-04-001` |
| Handoff 1 | `…/PARALLEL_BUSINESS_PROCESS_PROGRAM/P01_PROCURE_TO_PAY/P01_TO_P03_HANDOFF.md` — last modified **`fab37e0`, 2026-09-06** |
| Handoff 2 | `…/P01_P03_CORRECTION_HANDOFF.md` — last modified **`a6879cb`, 2026-09-05** |
| Also read | `P01_S18_PEER_DELTA_HANDOFF.md` — `8e7f94b`, 2026-09-05 |
| Closure Constitution | `48ee264fd74dcb0dee378789e56d028ad8bb6110` |
| Prior P03 closure prompt superseded | `c088f2f40cc1ee0e5881720192027991cd94eb80` |

**Supersession check performed** per `smeplus-supersession-binds-at-claim-level`: the base
handoff is **newer** (2026-09-06) than the correction delta (2026-09-05), so the correction
does **not** supersede it — they are complementary and both are binding. Reading only the
later-named file would have been wrong.

## 2. The claim that most changes P03 — P01 **withdraws** a routing to P03

> In round 6 P01 routed the valuation cost-explosion to **P03 as owner**, because the
> documents involved were manufacturing and unbuild. **P01 withdraws that routing.**

Root cause, from P01's direct source read:
`purchase_stock/models/stock_move.py::_get_price_unit`, series-16 core, three defects — **no
zero-guard on `remaining_qty`**, `invoice_lines` summed **unsigned** so refunds *increase* the
base, and **no cancelled-bill filter**. Entry condition `qty_invoiced > qty_received`. Live
firing set narrowed from 49 to a named **18** lines carrying `qty_received = 0.000000`.

> **"Manufacturing and unbuild documents propagate an already-corrupt unit cost; they do not
> originate it. P03 is a propagation route, not the owner."**

### P03's position on this

**P03 accepts the withdrawal and records that it independently reached the same conclusion.**
Round 4's `P03R-F-03` stated, before this handoff was read: *"Manufacturing did not originate
the corruption; it is the amplifier with the widest reach"*, and attributed the trigger to a
vendor receipt / bill revaluation with 8 of 30 corrupt rows on the receipt side.

**Two sessions, two directions, same answer.** P01 supplies the exact function and defect
list P03 could not see from its side; P03 supplies the amplification measurement P01 did not
make. Neither closes the other's half. `CQ-P03-04` is disposed on this basis.

## 3. What P01 hands P03, and what P01 keeps

| Item | Owner |
|---|---|
| The unconditional product-mismatch filter and its **13 live dropped rows** | **P01 retains** |
| The cost-explosion root cause and its 18 live lines | **P01 retains** |
| **The kit-specific question** — where phantom BoMs exist, does the kit purchase price difference reach RM/WIP/FG at all, and is the "manual" correction a defined procedure or an assumption in a comment? | **P03 receives** — disposed at `CQ-P03-02` §4 |
| How 18 bill lines came to name a different product than their PO line | **unowned**, named by P01, not P03's |

## 4. Corrections P03 must carry, and does

| P01 correction | P03 action |
|---|---|
| `purchase_mrp`'s filter has **no kit predicate** — the word "kit" exists only in the docstring; the filter is **unconditional** | Carried. P03 verified the same file in series 18: the filter is byte-identical and equally unconditional |
| `purchase_mrp` is **`auto_install: True`** — not opt-in | Carried |
| "LATENT" was **withdrawn**; the filter is **live**, 13 rows actively dropped | Carried. P03 does **not** re-classify it — it is P01's finding |
| "Skip" understates it — partial overlap **mis-scales** the correction | Carried into `CQ-P03-03` |
| The chain has a **third** participant, `stock_landed_costs`, inert here (0 landed-cost rows) but live wherever landed costs are used | Carried; P03 measured `stock_landed_cost` = **0 rows** in both manufacturing databases independently |
| Earlier "capitalised into inventory / no P&L variance" wording was **superseded** | **Not carried.** P03 uses only the final handoff's wording |
| Series-19 subcontract extra cost derives from the **bill first**, not the receipt; the series-18 credit-split construct is **gone** in 19 | Carried into `CQ-P03-03`; P03's `DEP-06` **remains open for series 18** as P01 states |

## 5. P01's declared limits, which bound everything P03 inherits

| Limit | Effect on P03 |
|---|---|
| **41 of 651 tables (6.3 %) extracted, no declared selection rule** (`GAP-P01-07`) | Every P01 negative P03 relies on carries this bound. P03 restates it rather than absorbing it |
| **Nothing executed at runtime in six rounds** | All P01 behaviour is source-and-records |
| The kit-latency finding is **single-deployment** | P03 does not generalise it |
| Series-16 source **never read for series 16 by P03** | See `MD-01` — and P01's cited series-16 root **does not resolve in P03's path set** (`MD-06`) |

## 6. Method control adopted from P01

> **An installed module that modifies a writer's INPUT can materially change behaviour
> without being a writer.**

`purchase_mrp` alters what the valuation writer receives while containing no assignment to
the valuation layer. **A writer enumeration scoped to writers is correct and not
sufficient.** P03 adopts this and applies it in `CQ-P03-02` §3.

## 7. What P03 did **not** do

- Did not execute, reopen or modify P01.
- Did not adopt any P01 claim without checking it against the published handoff — the two
  claims P03 could verify independently (the three-participant chain shape; `stock_landed_cost`
  = 0 rows) were verified and agree.
- Did not carry superseded P01 wording.
