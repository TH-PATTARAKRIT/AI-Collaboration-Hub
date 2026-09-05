# P03 — RM → WIP → SEMI/FG → COGS CAUSAL TRACE

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P03-03`. Business fact and accounting fact traced
separately.

---

## 1. Propagation of a cost delta entering RM

| # | Question | Answer |
|---|---|---|
| 1 | **When** does an RM cost delta propagate? | **At consumption, not at correction.** The value is read when `_cal_price` runs inside `_post_inventory`, i.e. when the order is marked done |
| 2 | **By which event/function?** | `_cal_price` → `total_cost = Σ(consumed layer values) + work-centre cost + extra cost`; then `finished_move.price_unit` |
| 3 | **Is lineage preserved?** | **No — it is embedded only in the changed unit cost.** No field links a finished-goods layer to the RM correction that changed its input. `P03C-F-01` |
| 4 | Does reversal reverse the same economic effect? | **No — see §3** |
| 5 | Can duplicate / zero / stranded cost arise? | **All three.** §4 |

## 2. Business fact vs accounting fact

| Layer | RM | WIP | Semi/FG | COGS |
|---|---|---|---|---|
| **Business fact** | material received and valued | **work performed** | goods produced | goods sold |
| **Accounting fact** | valuation layer | **none — no WIP object is posted in the manufacturing database** | finished valuation layer | **none — zero COGS lines** |

> **The two middle columns are where the accounting fact does not exist.** WIP has two
> unreconciled representations and the one that would post (`mrp_accountant`'s wizard) is
> **not installed** in the manufacturing deployment; COGS has never posted (P02, same
> database, independently counted 447,384 GL lines).
>
> **Business truth and accounting truth diverge for the whole middle of the chain.**

## 3. Reversal / unbuild — does it reverse the same economic effect?

**No.** Measured and read:

| Path | Behaviour |
|---|---|
| Build | FG valued at `total_cost` computed from the layers consumed at that moment |
| **Unbuild** | releases FG at **the first matching valuation layer's unit cost** (`DC-13`), not the layer the build actually consumed |

**Live consequence:** 12 of the 30 corrupt valuation rows are unbuild — **the single largest
origin group** — releasing product 11632 at −352,468,555,154.38 per unit five times over.

> `DC-13` is the **only** `DC-*` finding observed firing in production data, and it fires
> **into** the corruption rather than out of it. `FACT VERIFIED`.

**Version bound:** read in series 18. `MD-02` shows `_cal_price`'s cost source changed by
series 19; the unbuild release path was not separately differenced. Bounded accordingly.

## 4. Duplicate, zero and stranded cost

| Failure | Status in evidence |
|---|---|
| **Duplicate** | 7 latent mechanisms, **no mutual exclusion anywhere**; **none observed firing** |
| **Zero** | **Observed and universal** — conversion cost is zero in every examined deployment (`P03R-F-09`); and 49 completed finished moves carry **no valuation**, 280 carry **zero**, 1,386 consumptions are unvalued |
| **Stranded** | `extra_cost` capitalised and never relieved (`DC-03`, series ≤18); the production-account residues of `DC-03`/`DC-04` |
| **Exploded** | **Observed** — the third mode the duplicate/zero pair cannot express (`CQ-P03-04`) |

## 5. Semi-finished / multi-level

A semi-finished item enters its parent's `Σ consumed layer values` at whatever its own
`_cal_price` produced. **Every defect above compounds once per BOM level**, and the corruption
chain demonstrates it concretely: product 11556 (RM) → MO 4410 → products 11630 / 11632 /
11633 (FG) → unbuild → back into stock at a corrupt cost.

`SUPPORTED INTERPRETATION` for the general claim; `FACT VERIFIED` for the observed instance.

## 6. Disposition

> **`CQ-P03-03` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**, bounded by `MD-01`:
> the propagation *mechanism* is read in series 18 while the deployment runs series 16;
> the propagation *effects* are measured in the deployment itself and are unaffected.
>
> **`DEP-06`** (series-18 subcontract bill-difference) remains **UNRESOLVED**.
