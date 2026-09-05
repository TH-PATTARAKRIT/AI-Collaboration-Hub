# P03 → P08 (RECORD-TO-REPORT) — CLOSURE HANDOFF

**LAYER 1 — CLEAN ROOM.** **P03 defines no core-ledger architecture.**

---

## 1. The item P08 most needs

> **The inventory valuation subsidiary ledger and the general ledger have diverged.**
> Thirty valuation records carry values to ±1.5 × 10²¹. Twenty-five of them name a journal
> entry; **all twenty-five entries exist and carry entirely different, sane amounts —
> 25 mismatched, 0 matched.** The general ledger itself is **balanced**: 447,384 lines
> summing to exactly 0.00, with **no** line above 10¹².

P03 can demonstrate the divergence exhaustively and **cannot** demonstrate which write
produced the sane ledger figure — that needs the deployment's own generation of source, which
is unavailable, and a runtime reconstruction the safety veto forbids.

## 2. Handoff register

| # | Item | Class | P08 decides |
|---|---|---|---|
| 1 | Subsidiary ↔ general ledger divergence, 25 rows, with entry identifiers | **FACT VERIFIED** | which ledger is authoritative, and how divergence is **detected** rather than discovered |
| 2 | **Accounting-event identity.** The conversion-cost relief entry stamps a reference onto every contributing time record and **never reads it back as a guard**. The only protection is the caller's state filter | **FACT VERIFIED (absence)** | the event identity. **P09 raises the same dependency independently** — two processes, one gap |
| 3 | Three account resolvers at two levels for one work-in-progress concept; the component that would post the accrual is **not installed** in the deployment that manufactures | **FACT VERIFIED** | the WIP representation |
| 4 | The relief entry takes the **posting** date, not the event date — stable across both observable generations | **FACT VERIFIED** | period attribution. Same root cause P10 reports |
| 5 | **The near-cancellation property.** The thirty corrupt records net to −194.8 million against a gross exposure near 10²¹. **Any partial correction breaks the cancellation** | **FACT VERIFIED** | remediation sequencing is **above P08 and P03** — Boss |

## 3. Duplicate vs zero vs wrong financial effect

| Question | Measured answer |
|---|---|
| Duplicate financial effect from manufacturing? | **None observed.** The capitalise-and-relieve pair is matched |
| Zero financial effect? | **Yes, extensively** — conversion cost is zero in every examined deployment; 49 completed production receipts carry no valuation, 280 are valued zero, 1,386 consumptions unvalued |
| **Wrong** financial effect? | **Yes, two kinds** — misdirected (the relief credits the finished product's cost-of-sales account by default, on **every** configured resource examined) and **absurd** (§1) |

**The third row is the one to weigh.** A ledger that is balanced, duplicate-free and non-zero
can still be wrong, and both of P03's wrong-value findings pass every balance check.

## 4. Bound

Source-derived items are read in a **generation later than the deployment's own**, which P03
could not obtain. The **measured** items are read from the databases and are unaffected.
