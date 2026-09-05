# P01 — SUBCONTRACT PURCHASE HANDOFF

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.** Subcontract purchase was **outside** the previous round's denominator
(`ERR-P01-04`); this is its first P01 trace. **P01 makes no P03 decision.**

---

## 1. STATUS — CORRECTED TWICE

| Stage | Statement |
|---|---|
| Previous round | outside the module population entirely |
| Earlier this round | in the population, **"installed nowhere — latent"** |
| **Correct** | **ten modules, not three**, and **nine of the ten are installed** — in the fourth database, which this package wrongly recorded as unreadable (`ERR-P01-15`) |
| Exercised | **zero subcontract transactions anywhere** |
| Therefore | **`INSTALLED BUT NOT EXERCISED`** — not latent, not in use |

---

## 2. THE CHAIN, WHERE IT IS TRACEABLE

| Step | Owner | Note |
|---|---|---|
| Purchase of a subcontracted item | **P01** | an ordinary purchase order |
| Component supply to the subcontractor | **Inventory / P03** | goods leave without a sale |
| Subcontract receipt | **boundary** | the finished item returns and is valued |
| Consumption of components | **P03** | |
| WIP and conversion cost | **P03** | |
| Vendor bill for the service | **P01** | |
| AP | **P01** | |
| Finished-goods inventory | **Inventory** | |
| COGS | **P02 / Inventory** | on standing HOLD |

---

## 3. THE VALUATION CONSTRUCT — AND ITS DISAPPEARANCE

**v18:** on receipt of a subcontracted item the credit is **split in two** — a component-cost
line and a subcontracting-service-cost line — with the valuation price forced. The source's own
comment states that the service-cost figure **may not represent the real cost of the service**.
Classification: **FACT VERIFIED** for v18.

**v19: the construct is gone.** Classification: **CONTRADICTED for v19** — the v18 finding does
not carry forward.

---

## 4. A CORRECTION OWED TO PEER P03

P03's ownership premise cites the **v18** file. In v19 the extra cost is derived from the
**vendor bill first**, which **changes where the price difference lands**.

**This is routed to P03 and is not re-decided here.** P01 records the version divergence and the
consequence for P03's premise; P03 owns the conclusion.

---

## 5. THE BOUNDARY P01 ASSERTS

> **P01 owns the purchase of the subcontracting service and the resulting payable.
> P03 owns the conversion, the WIP and the cost model.
> The subcontract *receipt* is the boundary object, and it belongs to neither alone.**

Asserted as a position for P11 to reconcile. **Not a decision.**

---

## 6. OPEN

| ID | Item | Status |
|---|---|---|
| `SUB-01` | What v19 does instead of the split credit | **class C** |
| `SUB-02` | Whether the boundary receipt double-counts component cost and service cost | **HOLD — RUNTIME EVIDENCE REQUIRED**; zero transactions exist to observe |
| `SUB-03` | P03's response to §4 | **PEER DEPENDENCY OPEN** |
| `SUB-04` | `D4`'s subcontract configuration, beyond the module registry | **class C, known-reachable** |
